#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "liblzma::liblzma" for configuration "Release"
set_property(TARGET liblzma::liblzma APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(liblzma::liblzma PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/liblzma.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/liblzma.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS liblzma::liblzma )
list(APPEND _IMPORT_CHECK_FILES_FOR_liblzma::liblzma "${_IMPORT_PREFIX}/lib/liblzma.lib" "${_IMPORT_PREFIX}/bin/liblzma.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
