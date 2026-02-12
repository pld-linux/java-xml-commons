%define		subver	b2
%define		rel	11
%define		srcname	xml-commons
Summary:	Common code for Apache XML projects
Summary(pl.UTF-8):	Wspólny kod dla projektów Apache XML
Name:		java-%{srcname}
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/xml/commons/%{srcname}-%{version}.%{subver}.tar.gz
# Source0-md5:	6c6551ece56948ee535d5f5014489b8d
Patch0:		%{srcname}.build.patch
Patch1:		%{srcname}.manifest.patch
URL:		https://xerces.apache.org/xml-commons/
BuildRequires:	ant
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm >= 4.4.9-56
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
Provides:	java(xml-commons-apis) = %{version}
Obsoletes:	xml-commons < 1.0-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xml-commons is focused on common code and guidelines for xml projects.
Its first focus will be to organize and have common packaging for the
various externally-defined standards code relating to XML - things
like the DOM, SAX, and JAXP interfaces.

%description -l pl.UTF-8
Projekt xml-commons koncentruje się na wspólnym kodzie i wytycznych
dla projektów XML. Pierwszym celem będzie zorganizowanie i
spakietowanie kodu wspólnego dla różnych zewnętrznych standardów
związanych z XML-em - rzeczy takich jak DOM, SAX oraz interfejsy JAXP.

%package javadoc
Summary:	Online manual for xml-commons
Summary(pl.UTF-8):	Dokumentacja online dla xml-commons
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	xml-commons-javadoc < 1.0-1

%description javadoc
Documentation for xml-commons.

%description javadoc -l pl.UTF-8
Dokumentacja dla xml-commons.

%prep
%setup -q -n %{srcname}-%{version}.%{subver}

%{__sed} -i -e 's,\r$,,' build.xml
%{__sed} -i -e 's,\r$,,' java/which.xml
%{__sed} -i -e 's,\r$,,' java/external/build.xml

%patch -P0 -p1
%patch -P1 -p1

%build
%ant clean

%ant jars \
	-Dant.build.javac.target=1.8 \
	-Dant.build.javac.source=1.8

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install java/external/build/xml-apis.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-apis-%{version}.jar
install java/build/which.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-which-%{version}.jar

ln -s %{srcname}-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-apis.jar
ln -s %{srcname}-which-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-which.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a java/external/build/docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc KEYS README.html
%{_javadir}/xml-commons-apis-%{version}.jar
%{_javadir}/xml-commons-apis.jar
%{_javadir}/xml-commons-which-%{version}.jar
%{_javadir}/xml-commons-which.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
