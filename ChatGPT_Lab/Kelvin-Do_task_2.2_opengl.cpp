//external libraries that must be downloaded and imported in to the project, be in through a tree of folders, or cmake
#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>

int main() {
    // Initialize GLFW
    if (!glfwInit()) {
        std::cerr << "Failed to initialize GLFW" << std::endl;
        return -1;
    }

    // Set GLFW window hints
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GLFW_TRUE); // For macOS
#endif
    // Set window dimensions
    int width = 1080;
    int height = 720;

    // Create a GLFW window
    GLFWwindow* window = glfwCreateWindow(width, height, "example", nullptr, nullptr);
    if (!window) {
        std::cerr << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }   

    // Make the window's context current
    glfwMakeContextCurrent(window);

    // Load OpenGL function pointers using GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cerr << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    // Set the viewport size
    glViewport(0, 0, width, height);

    // Set the clear color for the window
    glClearColor(0.07f, 0.13f, 0.17f, 1.0f);

    // Main rendering loop
    while (!glfwWindowShouldClose(window)) {
        // Clear the color buffer
        glClear(GL_COLOR_BUFFER_BIT);

        // Swap the front and back buffers
        glfwSwapBuffers(window);

        // Poll for and process events
        glfwPollEvents();
    }

    // Cleanup: Destroy window and terminate GLFW
    glfwDestroyWindow(window);
    glfwTerminate();

    // Exit with success
    return 0;
}