from factory import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000, use_reloader=True, extra_files=['./blueprints/data/settings.yaml'])
