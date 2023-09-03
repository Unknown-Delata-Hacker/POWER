import subprocess


def run_command():
    # Install cmake
    try:
        subprocess.run(["pip", "install", "cmake"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing cmake: {e}")

    # Install dlib
    try:
        subprocess.run(["pip", "install", "dlib"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing dlib: {e}")

    # Install face_recognition
    try:
        subprocess.run(["pip", "install", "face_recognition"])
    except subprocess.CalledProcessError as e:
        print(f"Error installing face_recognition: {e}")

    # Verify the installation
    try:
        subprocess.run(["python", "-c", "import face_recognition; print('face_recognition library is installed and ready to use.')"])
    except subprocess.CalledProcessError as e:
        print(f"Error verifying installation: {e}")


def main():
    import face_recognition
    import streamlit as st

    st.write(
        """
    # My first app
    Hello *world!*
    """
    )


if __name__ == "__main__":
    run_command()
    main()
