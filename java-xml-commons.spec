%define		_beta	b2
%define		_rel	2
Summary:	Common code for XML projects
Summary(pl):	Wsp�lny kod dla projekt�w XML
Name:		xml-commons
Version:	1.0
Release:	0.%{beta}.1
License:	Apache Software License
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/xml/commons/%{name}-%{version}.%{_beta}.tar.gz
# Source0-md5:	6c6551ece56948ee535d5f5014489b8d
Patch0:		%{name}.build.patch
Patch1:		%{name}.manifest.patch
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.300
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

%description -l pl
Projekt xml-commons koncentruje si� na wsp�lnym kodzie i wytycznych
dla projekt�w XML. Pierwszym celem b�dzie zorganizowanie i
spakietowanie kodu wsp�lnego dla r�nych zewn�trznych standard�w
zwi�zanych z XML-em - rzeczy takich jak DOM, SAX oraz interfejsy JAXP.

%prep
%setup -q -n %{name}-%{version}.%{_beta}
%patch0 -p1
%patch1 -p1

# remove all binary libs and prebuilt javadocs
find -name "*.jar" -o -name "*.gz" | xargs rm -rf
rm -rf java/build java/external/build/docs/javadoc

%build
%ant jars

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install java/external/build/xml-apis.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-apis-%{version}.jar
install java/build/which.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-which-%{version}.jar

ln -sf %{name}-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-apis.jar
ln -sf %{name}-which-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-which.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS README.html java/external/build/docs/javadoc java/build/docs/javadocs
%{_javadir}/*.jar
