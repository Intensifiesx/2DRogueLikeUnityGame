	if (cd.superClass() != null) {
	    if (cd.name().equals(cd.superClass().typeName()))
		// NC6.java
		Error.error(cd, "Class '" + cd.name() + "' cannot extend itself.");
	    // If a superclass has a private default constructor, the 
	    // class cannot be extended.
	    ClassDecl superClass = (ClassDecl)classTable.get(cd.superClass().typeName());
	    SymbolTable st = (SymbolTable)superClass.methodTable.get("<init>");
	    ConstructorDecl ccd = (ConstructorDecl)st.get("");
	    if (ccd != null && ccd.getModifiers().isPrivate())
		// NC7.java
		Error.error(cd, "Class '" + superClass.className().getname() + "' cannot be extended because it has a private default constructor.");
	}
