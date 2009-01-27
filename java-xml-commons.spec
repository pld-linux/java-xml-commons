%define		_beta	b2
%define		_rel	3
%include	/usr/lib/rpm/macros.java
Summary:	Common code for XML projects
Summary(pl.UTF-8):	Wspólny kod dla projektów XML
Name:		xml-commons
Version:	1.0
Release:	0.%{_beta}.%{_rel}
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/xml/commons/%{name}-%{version}.%{_beta}.tar.gz
# Source0-md5:	6c6551ece56948ee535d5f5014489b8d
Patch0:		%{name}.build.patch
Patch1:		%{name}.manifest.patch
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	sed >= 4.0
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xml-commons is focused on common code and guidelines for xml projects.
Its first focus will be to organize and have common packaging for the
various externally-defined standards code relating to XML - things
like the DOM, SAX, and JAXP interfaces.

As the xml-commons community forms, we also hope to serve as a holding
area for other common xml-related utilities and code, and to help
promulgate common packaging, testing, documentation, and other
guidelines across all xml.apache.org subprojects.

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

%description javadoc
Documentation for xml-commons.

%description javadoc -l pl.UTF-8
Dokumentacja dla xml-commons.

%prep
%setup -q -n %{name}-%{version}.%{_beta}

%{__sed} -i -e 's,\r$,,' build.xml
%{__sed} -i -e 's,\r$,,' java/which.xml
%{__sed} -i -e 's,\r$,,' java/external/build.xml

%patch0 -p1
%patch1 -p1

# remove all binary libs and prebuilt javadocs
# find -name "*.jar" -o -name "*.gz" | xargs rm -rf
# rm -rf java/build java/external/build/docs/javadoc

%build
%ant jars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install java/external/build/xml-apis.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-apis-%{version}.jar
install java/build/which.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-which-%{version}.jar

ln -s %{name}-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-apis.jar
ln -s %{name}-which-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-which.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a java/external/build/docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc KEYS README.html
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
