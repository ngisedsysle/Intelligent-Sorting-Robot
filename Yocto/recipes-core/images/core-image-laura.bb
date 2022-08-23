SUMMARY = "A small image just capable of allowing a device to boot."

IMAGE_FEATURES += "ssh-server-openssh"
IMAGE_INSTALL_append = " nano openssh"
IMAGE_INSTALL = "packagegroup-core-boot ${CORE_IMAGE_EXTRA_INSTALL}"

IMAGE_INSTALL_append = " python3-paho-mqtt mosquitto libmosquitto1 libmosquittopp1 mosquitto-clients"

IMAGE_LINGUAS = " "

LICENSE = "MIT"

inherit core-image

IMAGE_ROOTFS_SIZE ?= "8192"
IMAGE_ROOTFS_EXTRA_SPACE_append = "${@bb.utils.contains("DISTRO_FEATURES", "systemd", " + 4096", "" ,d)}"