import subprocess


def run_command():
    try:
        subprocess.run(["xcode-select", "--install"], check=True)
        print("Command executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")


def main():
    import requests
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
