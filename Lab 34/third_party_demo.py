def main():
    try:
        import requests
    except ImportError:
        print("Optional dependency 'requests' is not installed.")
        print("Install it with: python3 -m pip install -r requirements.txt")
        return

    prepared = requests.Request(
        "GET",
        "https://api.github.com",
        params={"source": "lab34"},
    ).prepare()
    print("Requests version:", requests.__version__)
    print("Prepared HTTP method:", prepared.method)
    print("Prepared URL:", prepared.url)
    print("No network request was sent by this demo.")


if __name__ == "__main__":
    main()
