import random
import tkinter as tk
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image

distributions = [
    {
        'name': 'Ubuntu',
        'description': 'Ubuntu is a popular Linux distribution based on Debian. It is known for its ease of use and user-friendly interface.',
        'link': 'https://ubuntu.com/'
    },
    {
        'name': 'Fedora',
        'description': 'Fedora is a community-driven Linux distribution developed by the Fedora Project. It focuses on the latest technologies and is often considered a cutting-edge distribution.',
        'link': 'https://getfedora.org/'
    },
    {
        'name': 'Pop!_OS',
        'description': 'Pop!_OS is an Ubuntu-based Linux distribution created by System76. It provides a custom desktop environment and is optimized for productivity.',
        'link': 'https://pop.system76.com/'
    },
    {
        'name': 'Arch Linux',
        'description': 'Arch Linux is a lightweight and flexible Linux distribution that follows the rolling release model. It provides a minimalist and customizable system.',
        'link': 'https://archlinux.org/'
    },
    {
        'name': 'NixOS',
        'description': 'NixOS is a Linux distribution with a unique approach to package management and system configuration. It allows atomic upgrades and rollbacks of the entire system.',
        'link': 'https://nixos.org/'
    },
    {
        'name': 'OpenSUSE',
        'description': 'openSUSE is a community-driven Linux distribution sponsored by SUSE. It offers a stable and reliable system with different editions for different use cases.',
        'link': 'https://www.opensuse.org/'
    },
    {
        'name': 'Debian',
        'description': 'Debian is a widely used Linux distribution known for its stability and large package repository. It serves as the foundation for many other distributions.',
        'link': 'https://www.debian.org/'
    },
    {
        'name': 'Linux Mint',
        'description': 'Linux Mint is an elegant and user-friendly Linux distribution based on Ubuntu. It provides a familiar desktop environment and a variety of software.',
        'link': 'https://linuxmint.com/'
    },
    {
        'name': 'ElementaryOS',
        'description': 'ElementaryOS is a beautiful and beginner-friendly Linux distribution. It features a clean and intuitive interface inspired by macOS.',
        'link': 'https://elementary.io/'
    },
    {
        'name': 'Zorin OS',
        'description': 'Zorin OS is a Linux distribution designed to resemble Windows and macOS. It offers a familiar interface for users transitioning from those operating systems.',
        'link': 'https://zorinos.com/'
    },
    {
        'name': 'RHEL (Red Hat Enterprise Linux)',
        'description': 'RHEL is a commercial Linux distribution focused on stability and long-term support. It is widely used in enterprise environments.',
        'link': 'https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux'
    },
    {
        'name': 'Garuda Linux',
        'description': 'Garuda Linux is an Arch-based Linux distribution that aims to provide a complete and user-friendly system out of the box, with various desktop environments available.',
        'link': 'https://garudalinux.org/'
    }
]

def open_link(link):
    webbrowser.open(link)

def get_challenge_days():
    return random.randint(3, 90)

def get_daily_recommendation():
    return random.choice(distributions)

def show_recommendation():
    recommendation = get_daily_recommendation()
    challenge_days = get_challenge_days()

    def open_recommendation_link():
        open_link(recommendation['link'])

    message = (
        f"Name: {recommendation['name']}\n\n"
        f"Description: {recommendation['description']}\n\n"
        f"Link: {recommendation['link']}\n\n"
        f"Challenge: Use this distribution for {challenge_days} days!"
    )

    result = messagebox.showinfo('Linux Distribution Recommendation', message, icon=messagebox.INFO, type=messagebox.OKCANCEL)

    if result == messagebox.OK:
        open_link_choice = messagebox.askyesno('Open Link', 'Do you want to open the distribution link?')
        if open_link_choice:
            open_recommendation_link()

def run_linux_distribution_test():
    def show_test_results():
        test_result = "Based on your answers, the recommended distributions for you are:\n\n"

        familiar_with_linux = var_familiar_with_linux.get()
        is_mac = var_is_mac.get()
        play_games = var_play_games.get()
        like_mac_interface = var_like_mac_interface.get()
        like_windows_interface = var_like_windows_interface.get()
        latest_software = var_latest_software.get()
        prefer_old_reliable_software = var_prefer_old_reliable_software.get()

        if is_mac and play_games:
            test_result += "Fedora\nPop!_OS\nUbuntu\n\n"

        if familiar_with_linux and latest_software:
            test_result += "Arch Linux\nNixOS\n\n"

        if prefer_old_reliable_software:
            test_result += "Debian\nRHEL (Red Hat Enterprise Linux)\n\n"
        else:
            if like_windows_interface:
                test_result += "Linux Mint\n\n"

            if like_windows_interface and play_games:
                test_result += "Fedora\nGaruda Linux\nPop!_OS\n\n"

            if like_mac_interface:
                test_result += "Deepin\nElementaryOS\nFedora\n\n"

        messagebox.showinfo('Test Results', test_result.strip())

    test_window = tk.Toplevel()
    test_window.title('Test for a Suitable Linux Distribution')

    test_frame = tk.Frame(test_window, padx=20, pady=20)
    test_frame.pack()

    question_label1 = tk.Label(test_frame, text='Are you familiar with Linux and UNIX?')
    question_label1.pack()

    var_familiar_with_linux = tk.BooleanVar()
    option1_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_familiar_with_linux, value=True)
    option1_1.pack()
    option1_2 = tk.Radiobutton(test_frame, text='No', variable=var_familiar_with_linux, value=False)
    option1_2.pack()

    question_label2 = tk.Label(test_frame, text='Is your computer a Mac?')
    question_label2.pack()

    var_is_mac = tk.BooleanVar()
    option2_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_is_mac, value=True)
    option2_1.pack()
    option2_2 = tk.Radiobutton(test_frame, text='No', variable=var_is_mac, value=False)
    option2_2.pack()

    question_label3 = tk.Label(test_frame, text='Do you play games on your PC?')
    question_label3.pack()

    var_play_games = tk.BooleanVar()
    option3_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_play_games, value=True)
    option3_1.pack()
    option3_2 = tk.Radiobutton(test_frame, text='No', variable=var_play_games, value=False)
    option3_2.pack()

    question_label4 = tk.Label(test_frame, text='Do you like the Mac interface?')
    question_label4.pack()

    var_like_mac_interface = tk.BooleanVar()
    option4_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_like_mac_interface, value=True)
    option4_1.pack()
    option4_2 = tk.Radiobutton(test_frame, text='No', variable=var_like_mac_interface, value=False)
    option4_2.pack()

    question_label5 = tk.Label(test_frame, text='Do you like the Windows interface?')
    question_label5.pack()

    var_like_windows_interface = tk.BooleanVar()
    option5_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_like_windows_interface, value=True)
    option5_1.pack()
    option5_2 = tk.Radiobutton(test_frame, text='No', variable=var_like_windows_interface, value=False)
    option5_2.pack()

    question_label6 = tk.Label(test_frame, text='Do you want the latest software?')
    question_label6.pack()

    var_latest_software = tk.BooleanVar()
    option6_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_latest_software, value=True)
    option6_1.pack()
    option6_2 = tk.Radiobutton(test_frame, text='No', variable=var_latest_software, value=False)
    option6_2.pack()

    question_label7 = tk.Label(test_frame, text='Do you prefer old but reliable software?')
    question_label7.pack()

    var_prefer_old_reliable_software = tk.BooleanVar()
    option7_1 = tk.Radiobutton(test_frame, text='Yes', variable=var_prefer_old_reliable_software, value=True)
    option7_1.pack()
    option7_2 = tk.Radiobutton(test_frame, text='No', variable=var_prefer_old_reliable_software, value=False)
    option7_2.pack()

    test_button = tk.Button(test_window, text='Submit', command=show_test_results)
    test_button.pack(pady=10)

def show_linux_benefits():
    benefits = (
        "GNU/Linux is a free and open-source operating system that is based on the Linux kernel and the GNU software. "
        "It is a popular alternative to proprietary operating systems such as Windows and macOS, which have more "
        "restrictions and limitations on their users. Some of the benefits of Linux compared to Windows and macOS are:\n\n"
        "- Linux is more secure and less vulnerable to viruses and malware, as it has a robust permission system and a "
        "large community of developers who constantly update and patch the system.\n\n"
        "- Linux is more customizable and flexible, as it offers a variety of distributions, desktop environments, "
        "applications, and settings that can suit different needs and preferences of the users.\n\n"
        "- Linux is more efficient and reliable, as it consumes less resources and runs faster than Windows and macOS."
    )

    messagebox.showinfo('Why Linux?', benefits)

def main():
    root = tk.Tk()
    root.title('LinuxDistroChooser')

    # Set the default size of the main window
    root.geometry('400x400')

    # Load background image
    background_image = Image.open('background.png')
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a label with the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack()

    # Load Tux penguin image
    tux_image = Image.open('tux.png')
    tux_image = tux_image.resize((123, 145), Image.BILINEAR)
    tux_photo = ImageTk.PhotoImage(tux_image)

    # Display Tux penguin image
    tux_label = tk.Label(frame, image=tux_photo)
    tux_label.pack()

    recommendation_button = tk.Button(frame, text='Get Recommendation', command=show_recommendation)
    recommendation_button.pack(pady=10)

    test_button = tk.Button(frame, text='Test for a Suitable Linux Distribution', command=run_linux_distribution_test)
    test_button.pack(pady=10)

    benefits_button = tk.Button(frame, text='Learn about the benefits of Linux!', command=show_linux_benefits)
    benefits_button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    main()
