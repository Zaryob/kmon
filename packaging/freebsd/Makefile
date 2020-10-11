# New ports collection makefile for:	kmon
# Date created:				16 March 2010
# Whom:					Kenneth Salerno <kennethsalerno@yahoo.com>
#
# $FreeBSD$
#
# This port is self contained in the files directory.
#

PORTNAME=	kmon
PORTVERSION=	0.8.freebsd.noarch
CATEGORIES=	sysutils
MASTER_SITES=	# none
DISTFILES=	# none

MAINTAINER=	KennethSalerno@yahoo.com
COMMENT=	Ken's MONitor

NO_BUILD=	yes

PLIST_FILES=	bin/kmon

MAN8=		kmon.8

.include <bsd.port.pre.mk>

do-install:
	${INSTALL_SCRIPT} ${FILESDIR}/kmon ${PREFIX}/bin/kmon
	${INSTALL_MAN} ${FILESDIR}/kmon.8 ${MAN8PREFIX}/man/man8

.include <bsd.port.post.mk>
