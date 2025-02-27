wolfCrypt-py Release 5.4.0 (July 13, 2022)
==========================================

New Features
------------

* Update to wolfCrypt 5.4.0 C library
* Add GitHub Actions support, remove Travis CI

Fixes
-----

* Fixups for PyPi
* Remove some of the CMake hack due to things moved into wolfSSL CMakeLists.txt

wolfCrypt-py Release 5.3.0 (May 10, 2022)
=========================================

New Features
------------

* Update to wolfCrypt 5.3.0
* Build completely refactored to be more Python-like and easier to use
* Added support for SHA3
* Added support for ChaCha stream cipher
* Add support for RSA private keys in PKCS #8 format
* Add module pwdbased.py and expose wc_PBKDF2
* Modifications to make wolfCrypt-py work with FIPS ready and FIPS v5
* Add support for ed448
* Add a pem_to_der function and support for PEM RSA keys
* Add signature generation and verification
* Enabled pwdbased by default
* Windows support added
* Added support for AES-CTR
* Add support for AES GCM streaming
* Add RSA OAEP and PSS padding
* Add get_aad() function

Fixes
-----

* Documentation improvements
