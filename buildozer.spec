[app]
title = Calc
package.name = calc
package.domain = com.calc
version = 1.0.0

source.dir = .
source.include_exts = py

requirements = python3,kivy,flask

orientation = portrait
fullscreen = 0

android.minapi = 21
android.maxapi = 33
android.targetapi = 31
android.api = 31

android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
build_dir = .buildozer
bin_dir = bin
