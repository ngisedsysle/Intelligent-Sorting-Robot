FILESEXTRAPATHS_prepend := "${THISDIR}:"

SRC_URI += "\
	     file://files \
	"

do_install_append(){
	install -m 0755 ${WORKDIR}/files/mosquitto.conf \
			${D}${sysconfdir}/mosquitto/mosquitto.conf
}
