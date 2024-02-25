// Check if the class extends itself
if (cd.name().equals(cd.superClass().typeName())) {
    Error.error(cd, "Class '" + cd.name() + "' cannot extend itself.");
}

// Check if the superclass has a private default constructor
ClassDecl superClass = (ClassDecl) classTable.get(cd.superClass().typeName());
if (superClass != null) {
    ConstructorDecl constructor = superClass.getConstructor();
    if (constructor != null && constructor.isPrivate()) {
        Error.error(cd, "Class '" + superClass.name() + "' cannot be extended because it has a private default constructor.");
    }
}
