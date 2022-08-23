SUMMARY = "Handling the subscriber and the publisher for MQTT"
SECTION = "custom"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

SRC_URI += "file://subscriber.py"
SRC_URI += "file://publisher.py"
SRC_URI += "file://publisher_photo.py"

RDEPENDS_${PN} += "python3-core"
RDEPENDS_${PN} += "python3-modules"

do_install() {
    install -d ${D}${bindir}
    install -m 0777 ${WORKDIR}/subscriber.py ${D}${bindir}
    install -m 0777 ${WORKDIR}/publisher.py ${D}${bindir}
    install -m 0777 ${WORKDIR}/publisher_photo.py ${D}${bindir}
}

FILES_${PN} += "${bindir}/subscriber.py"
FILES_${PN} += "${bindir}/publisher.py"
FILES_${PN} += "${bindir}/publisher_photo.py"
