%define		beta		b2

Summary:        Common code for XML projects
Summary(pl):	Wspólny kod dla projektów XML
Name:           xml-commons
Version:        1.0
Release:       	0.%{beta}.1
License:        Apache Software License
Group:		Development/Languages/Java
Source0:        http://xml.apache.org/dist/commons/xml-commons-1.0.b2.tar.gz
# Source0-md5:	6c6551ece56948ee535d5f5014489b8d
Patch0:         xml-commons.build.patch
Patch1:         xml-commons.manifest.patch
URL:            http://xml.apache.org/commons/
BuildRequires:  jakarta-ant
BuildArch:      noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	/usr/share/java

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
Projekt xml-commons koncentruje siê na wspólnym kodzie i wytycznych
dla projektów XML. Pierwszym celem bêdzie zorganizowanie i
spakietowanie kodu wspólnego dla ró¿nych zewnêtrznych standardów
zwi±zanych z XML - rzeczy takich jak DOM, SAX oraz interfejsy JAXP.

%prep
%setup -q -n %{name}-%{version}.%{beta}
%patch0 -p1
%patch1 -p1
# remove all binary libs and prebuilt javadocs
rm -rf `find . -name "*.jar" -o -name "*.gz"`
rm -rf java/build java/external/build/docs/javadoc

%build
ant jars

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javalibdir}

cp java/external/build/xml-apis.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-apis-%{version}.jar
cp java/build/which.jar $RPM_BUILD_ROOT%{_javalibdir}/%{name}-which-%{version}.jar

ln -sf %{name}-apis-%{version}.jar $RPM_BUILD_ROOT/%{_javalibdir}/%{name}-apis.jar
ln -sf %{name}-which-%{version}.jar $RPM_BUILD_ROOT/%{_javalibdir}/%{name}-which.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc KEYS README.html java/external/build/docs/javadoc java/build/docs/javadocs
%{_javalibdir}/*.jar
