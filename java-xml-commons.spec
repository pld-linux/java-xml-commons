%{?use_default_jdk:%use_default_jdk 8}

Summary:	Common XML APIs for Java (DOM, SAX, JAXP)
Summary(pl.UTF-8):	Wspólne API XML dla Javy (DOM, SAX, JAXP)
Name:		java-xml-commons
Version:	1.4.01
Release:	2
License:	Apache v2.0
Group:		Libraries/Java
# Use OBS repacked source because the Apache external tarball lacks the
# full Ant-oriented external/ layout (build.xml + docs) expected by distro builds.
# Original upstream release URL (source-only layout):
# https://archive.apache.org/dist/xml/commons/source/xml-commons-external-%{version}-src.tar.gz
Source0:	https://build.opensuse.org/public/source/openSUSE:Factory/xml-commons-apis/xml-commons-external-%{version}-src.tar.xz
URL:		https://xerces.apache.org/xml-commons/
BuildRequires:	ant
%buildrequires_jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
Requires:	jpackage-utils
Provides:	java(xml-commons-apis) = %{version}
Obsoletes:	xml-commons < 1.0-1
BuildRequires:	rpmbuild(macros) >= 1.556
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xml-commons-external provides Java XML standards APIs shared by many
projects, including DOM, SAX, and JAXP interfaces.

%description -l pl.UTF-8
Pakiet xml-commons-external dostarcza wspólne standardowe API XML dla
wielu projektów Java, w tym interfejsy DOM, SAX oraz JAXP.

%package javadoc
Summary:	API documentation for xml-commons
Summary(pl.UTF-8):	Dokumentacja API dla xml-commons
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	xml-commons-javadoc < 1.0-1

%description javadoc
API documentation for xml-commons.

%description javadoc -l pl.UTF-8
Dokumentacja API dla xml-commons.

%prep
%setup -q -n external

%build
%ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install -pm 644 build/xml-apis.jar $RPM_BUILD_ROOT%{_javadir}/xml-commons-apis-%{version}.jar
ln -s xml-commons-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xml-commons-apis.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/xml-commons-%{version}
cp -a build/docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/xml-commons-%{version}
ln -s xml-commons-%{version} $RPM_BUILD_ROOT%{_javadocdir}/xml-commons # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs xml-commons-%{version} %{_javadocdir}/xml-commons

%files
%defattr(644,root,root,755)
%doc LICENSE NOTICE README.dom.txt README.sax.txt LICENSE.sax.txt LICENSE.sac.html LICENSE.dom-software.txt LICENSE.dom-documentation.txt
%{_javadir}/xml-commons-apis-%{version}.jar
%{_javadir}/xml-commons-apis.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/xml-commons-%{version}
%ghost %{_javadocdir}/xml-commons
