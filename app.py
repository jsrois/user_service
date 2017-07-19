import argparse

from user_service.user_service import app


def run_application(options):
    app.run(**options)


def main():
    parser = argparse.ArgumentParser(
        description="An app to demonstrate Video Analytics capabilities running on a server")
    parser.add_argument(
        "--port", "-p",
        type=int,
        help="Port to listen for incoming requests",
        default=8080,
    )

    parser.add_argument(
        "--debug", "-d",
        action='store_true',
        help="Launch debug mode",
    )

    args = parser.parse_args()

    options = dict(
        host='127.0.0.1',
        debug=args.debug,
        port=args.port,
        threaded=True
    )
    run_application(options)


if __name__ == "__main__":
    main()