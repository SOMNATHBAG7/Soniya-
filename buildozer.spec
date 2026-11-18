[app]

title = SONIYA
package.name = soniya
package.domain = com.soniya

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 35
android.minapi = 23
android.ndk = 25b
android.archs = arm64-v8a

p4a.branch = develop

[buildozer]

log_level = 2
warn_on_root = 1
