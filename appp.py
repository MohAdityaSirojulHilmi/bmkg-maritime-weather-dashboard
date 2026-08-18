import os
import csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from flask import Flask, render_template


# ============================================================
# 1. KONFIGURASI FLASK
# ============================================================

app = Flask(__name__)

# Folder tempat app.py berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Folder static
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Folder templates
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


# ============================================================
# 2. LOKASI FILE DATA
# ============================================================

CSV_AWS = os.path.join(BASE_DIR, "Data_AWS.csv")

EXCEL_WARNING = os.path.join(
    BASE_DIR,
    "daftar_warning_ffbul_.xlsx"
)

AWS_IMAGE = os.path.join(
    STATIC_DIR,
    "aws.png"
)


# ============================================================
# 3. MEMBUAT FOLDER STATIC JIKA BELUM ADA
# ============================================================

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)


# ============================================================
# 4. MEMBACA DATA AWS
# ============================================================

def baca_data_aws():

    if not os.path.exists(CSV_AWS):
        raise FileNotFoundError(
            f"File Data_AWS.csv tidak ditemukan di:\n{CSV_AWS}"
        )

    df = pd.read_csv(
        CSV_AWS,
        sep=";"
    )

    return df


# ============================================================
# 5. MEMBUAT GRAFIK AWS
# ============================================================

def buat_grafik_aws():

    df = baca_data_aws()

    # --------------------------------------------------------
    # Ambil 1440 data terakhir
    # --------------------------------------------------------

    data = df.tail(1440).copy()

    # --------------------------------------------------------
    # Konversi waktu
    # --------------------------------------------------------

    data["datetime"] = pd.to_datetime(
        data["waktu"],
        errors="coerce"
    )

    data["jam"] = data["datetime"].dt.strftime("%H:%M")

    # --------------------------------------------------------
    # Pastikan kolom numerik
    # --------------------------------------------------------

    kolom_numerik = [
        "winddir",
        "windspeed",
        "temp",
        "rh",
        "pressure",
        "waterlevel"
    ]

    for kolom in kolom_numerik:

        if kolom in data.columns:

            data[kolom] = pd.to_numeric(
                data[kolom],
                errors="coerce"
            )

    # --------------------------------------------------------
    # Hapus data waktu yang tidak valid
    # --------------------------------------------------------

    data = data.dropna(
        subset=["datetime"]
    )

    # ========================================================
    # FIGURE
    # ========================================================

    fig = plt.figure(
        figsize=(12, 6)
    )

    # ========================================================
    # GRAFIK 1
    # WIND SPEED + WIND DIRECTION
    # ========================================================

    ax0 = plt.subplot2grid(
        (2, 2),
        (0, 0),
        rowspan=2,
        projection="polar"
    )

    arah_angin = data["winddir"]
    kecepatan_angin = data["windspeed"]

    # Konversi arah ke radian
    arah_radian = np.radians(
        -(90 - arah_angin)
    )

    warna = kecepatan_angin

    c = ax0.scatter(
        arah_radian,
        kecepatan_angin,
        c=warna,
        cmap="plasma",
        alpha=0.75,
        vmin=0,
        vmax=10
    )

    # Utara di atas
    ax0.set_theta_zero_location("N")

    # Arah searah jarum jam
    ax0.set_theta_direction(-1)

    # Colorbar
    cb = plt.colorbar(
        c,
        ax=ax0,
        location="left"
    )

    cb.set_label(
        "Wind Speed (m/s)"
    )

    ax0.set_title(
        "Wind Speed and Wind Direction"
    )

    # Arah mata angin
    ax0.set_xticks(
        np.radians(
            [0, 45, 90, 135, 180, 225, 270, 315]
        )
    )

    ax0.set_xticklabels(
        [
            "N",
            "NE",
            "E",
            "SE",
            "S",
            "SW",
            "W",
            "NW"
        ]
    )

    # Hilangkan angka radius
    ax0.set_yticklabels([])

    # ========================================================
    # GRAFIK 2
    # TEMPERATURE + HUMIDITY + PRESSURE
    # ========================================================

    ax1 = plt.subplot2grid(
        (2, 2),
        (0, 1)
    )

    # --------------------------------------------------------
    # Temperature
    # --------------------------------------------------------

    ax1.plot(
        data["datetime"],
        data["temp"].rolling(
            window=100,
            min_periods=1
        ).mean(),
        label="Temperature"
    )

    ax1.set_xlabel(
        "Time"
    )

    ax1.set_ylabel(
        "Temperature"
    )

    ax1.legend(
        loc="lower left"
    )

    ax1.set_title(
        "Temperature, Humidity, and Pressure"
    )

    ax1.set_ylim(
        20,
        40
    )

    # --------------------------------------------------------
    # X axis
    # --------------------------------------------------------

    jumlah_tick = min(
        12,
        len(data)
    )

    if jumlah_tick > 1:

        xticks_indices = np.linspace(
            0,
            len(data) - 1,
            jumlah_tick,
            dtype=int
        )

        ax1.set_xticks(
            data["datetime"].iloc[
                xticks_indices
            ]
        )

        ax1.set_xticklabels(
            data["jam"].iloc[
                xticks_indices
            ],
            rotation=45
        )

    ax1.grid(True)

    # ========================================================
    # HUMIDITY
    # ========================================================

    ax2 = ax1.twinx()

    ax2.plot(
        data["datetime"],
        data["rh"].rolling(
            window=100,
            min_periods=1
        ).mean(),
        label="Humidity"
    )

    ax2.set_ylabel(
        "Humidity"
    )

    ax2.legend(
        loc="lower right"
    )

    ax2.set_ylim(
        50,
        90
    )

    # ========================================================
    # PRESSURE
    # ========================================================

    ax4 = ax1.twinx()

    ax4.plot(
        data["datetime"],
        data["pressure"].rolling(
            window=100,
            min_periods=1
        ).mean(),
        label="Pressure"
    )

    ax4.spines[
        "right"
    ].set_position(
        ("outward", 60)
    )

    ax4.set_ylabel(
        "Pressure"
    )

    ax4.legend(
        loc="upper center"
    )

    ax4.set_ylim(
        995,
        1015
    )

    # ========================================================
    # GRAFIK 3
    # WATER LEVEL
    # ========================================================

    ax3 = plt.subplot2grid(
        (2, 2),
        (1, 1)
    )

    ax3.plot(
        data["datetime"],
        data["waterlevel"].rolling(
            window=100,
            min_periods=1
        ).mean()
    )

    ax3.set_title(
        "Water Level"
    )

    ax3.set_xlabel(
        "Time"
    )

    ax3.set_ylabel(
        "Water Level"
    )

    ax3.set_ylim(
        0,
        6
    )

    if jumlah_tick > 1:

        ax3.set_xticks(
            data["datetime"].iloc[
                xticks_indices
            ]
        )

        ax3.set_xticklabels(
            data["jam"].iloc[
                xticks_indices
            ],
            rotation=45
        )

    ax3.grid(True)

    # ========================================================
    # RAPATKAN LAYOUT
    # ========================================================

    plt.tight_layout()

    # ========================================================
    # SIMPAN GAMBAR
    # ========================================================

    plt.savefig(
        AWS_IMAGE,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)


# ============================================================
# 6. MENGAMBIL NILAI TERAKHIR DATA AWS
# ============================================================

def get_last_values():

    if not os.path.exists(CSV_AWS):

        raise FileNotFoundError(
            f"File Data_AWS.csv tidak ditemukan:\n{CSV_AWS}"
        )

    last_values = {}

    with open(
        CSV_AWS,
        "r",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(
            file,
            delimiter=";"
        )

        columns = reader.fieldnames

        if not columns:

            raise ValueError(
                "Data_AWS.csv tidak memiliki header kolom."
            )

        # Inisialisasi
        for column in columns:

            last_values[column] = None

        # Ambil baris terakhir
        for row in reader:

            for column in columns:

                last_values[column] = row[column]

    return last_values


# ============================================================
# 7. MENGAMBIL INFORMASI PERINGATAN DINI
# ============================================================

def get_warning_info():

    # --------------------------------------------------------
    # Cek file Excel
    # --------------------------------------------------------

    if not os.path.exists(EXCEL_WARNING):

        print(
            "PERINGATAN: File daftar_warning_ffbul_.xlsx "
            "tidak ditemukan."
        )

        return (
            None,
            None,
            None,
            None,
            "Tidak ada data peringatan dini."
        )

    # --------------------------------------------------------
    # Baca Excel
    # --------------------------------------------------------

    data = pd.read_excel(
        EXCEL_WARNING
    )

    # --------------------------------------------------------
    # Cek kolom
    # --------------------------------------------------------

    if "Waktu" not in data.columns:

        raise ValueError(
            "Kolom 'Waktu' tidak ditemukan "
            "di daftar_warning_ffbul_.xlsx"
        )

    if "Kecepatan" not in data.columns:

        raise ValueError(
            "Kolom 'Kecepatan' tidak ditemukan "
            "di daftar_warning_ffbul_.xlsx"
        )

    # --------------------------------------------------------
    # Konversi waktu
    # --------------------------------------------------------

    data["Waktu"] = pd.to_datetime(
        data["Waktu"],
        errors="coerce"
    )

    # Hapus waktu kosong
    data = data.dropna(
        subset=["Waktu"]
    )

    # --------------------------------------------------------
    # Kalau data kosong
    # --------------------------------------------------------

    if data.empty:

        return (
            None,
            None,
            None,
            None,
            "Tidak ada data peringatan dini."
        )

    # --------------------------------------------------------
    # Konversi kecepatan menjadi numerik
    # --------------------------------------------------------

    data["Kecepatan"] = pd.to_numeric(
        data["Kecepatan"],
        errors="coerce"
    )

    data_kecepatan = data.dropna(
        subset=["Kecepatan"]
    )

    # --------------------------------------------------------
    # Tanggal minimum dan maksimum
    # --------------------------------------------------------

    tanggal_minimal = (
        data["Waktu"].min().date()
    )

    tanggal_maksimal = (
        data["Waktu"].max().date()
    )

    # --------------------------------------------------------
    # Jam minimum dan maksimum
    # --------------------------------------------------------

    jam_minimal = (
        data["Waktu"].min().time()
    )

    jam_maksimal = (
        data["Waktu"].max().time()
    )

    # --------------------------------------------------------
    # Kecepatan angin
    # --------------------------------------------------------

    if not data_kecepatan.empty:

        kecepatan_minimal = (
            data_kecepatan["Kecepatan"].min()
        )

        kecepatan_maksimal = (
            data_kecepatan["Kecepatan"].max()
        )

        kecepatan_angin = (
            "Berpotensi terjadi kecepatan angin "
            f"dengan rentang: "
            f"{kecepatan_minimal:.2f} "
            f"hingga "
            f"{kecepatan_maksimal:.2f} m/s"
        )

    else:

        kecepatan_angin = (
            "Data kecepatan angin tidak tersedia."
        )

    return (
        tanggal_minimal,
        tanggal_maksimal,
        jam_minimal,
        jam_maksimal,
        kecepatan_angin
    )


# ============================================================
# 8. HALAMAN UTAMA
# ============================================================

@app.route("/")
def index():

    try:

        # ----------------------------------------------------
        # Ambil data AWS terakhir
        # ----------------------------------------------------

        last_values = get_last_values()

        # ----------------------------------------------------
        # Ambil informasi peringatan
        # ----------------------------------------------------

        (
            tanggal_minimal,
            tanggal_maksimal,
            jam_minimal,
            jam_maksimal,
            kecepatan_angin
        ) = get_warning_info()

        # ----------------------------------------------------
        # Format peringatan
        # ----------------------------------------------------

        if tanggal_minimal is not None:

            tanggal_minimal_html = (
                tanggal_minimal.strftime("%Y-%m-%d")
            )

            tanggal_maksimal_html = (
                tanggal_maksimal.strftime("%Y-%m-%d")
            )

            jam_minimal_html = (
                jam_minimal.strftime("%H:%M:%S")
            )

            jam_maksimal_html = (
                jam_maksimal.strftime("%H:%M:%S")
            )

        else:

            tanggal_minimal_html = "-"
            tanggal_maksimal_html = "-"
            jam_minimal_html = "-"
            jam_maksimal_html = "-"

        # ----------------------------------------------------
        # Render HTML
        # ----------------------------------------------------

        return render_template(
            "fix.html",

            windspeed=last_values.get(
                "windspeed",
                "-"
            ),

            winddir=last_values.get(
                "winddir",
                "-"
            ),

            temp=last_values.get(
                "temp",
                "-"
            ),

            rh=last_values.get(
                "rh",
                "-"
            ),

            pressure=last_values.get(
                "pressure",
                "-"
            ),

            watertemp=last_values.get(
                "watertemp",
                "-"
            ),

            waterlevel=last_values.get(
                "waterlevel",
                "-"
            ),

            tanggal_minimal=tanggal_minimal_html,

            jam_minimal=jam_minimal_html,

            tanggal_maksimal=tanggal_maksimal_html,

            jam_maksimal=jam_maksimal_html,

            kecepatan_angin=kecepatan_angin
        )

    except Exception as e:

        print("\n===================================")
        print("ERROR:")
        print(e)
        print("===================================\n")

        return (
            f"<h1>Terjadi Error</h1>"
            f"<pre>{e}</pre>"
        ), 500


# ============================================================
# 9. MENJALANKAN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("")
    print("==============================================")
    print("       DASHBOARD MONITORING MARITIM")
    print("==============================================")
    print("")
    print("Lokasi app.py:")
    print(BASE_DIR)
    print("")
    print("File Data AWS:")
    print(CSV_AWS)
    print("")
    print("File Warning:")
    print(EXCEL_WARNING)
    print("")
    print("Folder Static:")
    print(STATIC_DIR)
    print("")
    print("==============================================")

    # --------------------------------------------------------
    # Cek file Data AWS
    # --------------------------------------------------------

    if os.path.exists(CSV_AWS):

        print("✓ Data_AWS.csv ditemukan.")

    else:

        print("✗ Data_AWS.csv TIDAK ditemukan!")

    # --------------------------------------------------------
    # Cek file warning
    # --------------------------------------------------------

    if os.path.exists(EXCEL_WARNING):

        print("✓ daftar_warning_ffbul_.xlsx ditemukan.")

    else:

        print(
            "⚠ daftar_warning_ffbul_.xlsx "
            "tidak ditemukan."
        )

    # --------------------------------------------------------
    # Buat grafik AWS
    # --------------------------------------------------------

    try:

        print("")
        print("Membuat grafik AWS...")

        buat_grafik_aws()

        print("✓ Grafik AWS berhasil dibuat:")
        print(AWS_IMAGE)

    except Exception as e:

        print("")
        print("⚠ Gagal membuat grafik AWS:")
        print(e)

    # --------------------------------------------------------
    # Jalankan Flask
    # --------------------------------------------------------

    print("")
    print("==============================================")
    print("Flask berjalan di:")
    print("http://127.0.0.1:5000")
    print("==============================================")
    print("")

    app.run(
        debug=True
    )