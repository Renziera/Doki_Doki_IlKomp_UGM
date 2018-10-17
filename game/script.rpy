# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Renz")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    "Halo"

    "Selamat datang di Petualangan Rafel"

    s "Perkenalkan, saya Renz, guide kamu disini dan bukan sepupu sepongbob"

    s "Ini adalah visual novel paling legendaris yang pernah ada"

    s "Apakah anda tahu apa itu visual novel ?"

    menu:
        "Ya, saya tahu":
            jump tahu

        "Apa tuh ?":
            jump gaktahu

    label gaktahu:

        s "Baiklah akan saya jelaskan sedikit"

        s "Visual Novel adalah cerita yang disajikan dalam bentuk visual"

        s "Biasanya terdapat pula choices atau pilihan yang dapat mengubah jalan cerita"

        s "Kalian harus berusaha mendapatkan semua flag untuk good ending dan menghindari bad ending"

        s "Nama karakter yang sedang berbicara ditampilkan di atas dialognya"

        s "Sedangkan yang tidak ada namanya berarti monolog atau pikiran tokoh utama yang kalian mainkan"

        "Seperti ini"

        s "Sepertinya cukup, untuk info lebih lanjut silahkan tanyakan pada wibu terdekat"

        jump tahu

    label tahu:

        s "Baik, langsung saja kita mulai"

        s "Petualangan Rafel dimulai dalam..."

        s "3..."

        s "2..."

        s "1..."

        s "0"

        s "-1"

        s "wkwk"

        "Namaku Rafel, aku adalah maba IlKomp UGM '18 yang langganan jadi bahan bully teman-teman"

        "Meskipun begitu, aku tetap semangat berangkat ke kampus setiap hari"

        "Ah akhirnya tiba di MIPA"

        scene selasar1

        "Eh ada Juan"

        "Rafel" "Selamat pagi Juan"

        show juan :
            zoom 0.7 xpos 0.5 ypos 0

        "Juan" "Eh Rafel ngapain lu? Ngajak ribut?"

        "Rafel" "Eh engga e"

        "Juan" "Mau gelud ?"

        menu:
            "Hayuk gelud kuy":
                
                show juan with hpunch

                "Karena tak kuasa melawan Juan, Rafel segera dilarikan ke GMC"

                ".:. Bad End"

                return

            "Engga ah gak baik itu":
                "Rafel" "Gelud itu gak ada gunanya e"

        "Juan" "Yaudah sana"

        "Rafel" "Aku ke kelas dulu e"

        hide juan

        "Aduh harus cepat ini mau telat"

        scene tangga1

        "Gak sabar aku ketemu anak kimia manis-manis"



    # This ends the game.

    return
