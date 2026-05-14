
setup(
    name="zodiac",
    packages=["zodiac"],
    entry_points={
        "console_scripts": [
            "zodiac=zodiac.zodiac_cli:run_cli"
        ]
    },
    ...
)
