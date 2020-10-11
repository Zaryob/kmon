# $OpenBSD$

COMMENT=	Ken's MONitor

VERSION=	0.8.openbsd.noarch
DISTNAME=	kmon-${VERSION}
PKGNAME=	${DISTNAME:S/_/-/}
CATEGORIES=	sysutils

MAINTAINER=     Kenneth Salerno <kennethsalerno@yahoo.com>

PERMIT_PACKAGE_CDROM=	Yes
PERMIT_PACKAGE_FTP=	Yes
PERMIT_DISTFILES_CDROM=	Yes
PERMIT_DISTFILES_FTP=	Yes

SRCBALL_NAME=	${DISTNAME}
WRKDIST=	${WRKDIR}/${SRCBALL_NAME}

NO_REGRESS=	Yes

do-install:
	${INSTALL_PROGRAM} ${WRKBUILD}/kmon ${PREFIX}/bin
	${INSTALL_MAN} ${WRKSRC}/kmon.8 ${PREFIX}/man/man8/kmon.8

.include <bsd.port.mk>
