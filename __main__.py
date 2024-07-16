import cherrypy

class FibonacciService:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self, n):
        try:
            n = int(n)
        except ValueError:
            return {"error": "Invalid input. Please provide an integer value."}

        if n < 0:
            return {"error": "Input must be a non-negative integer."}

        return {"fibonacci": self.fibonacci(n)}

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            return b

if __name__ == '__main__':
    cherrypy.quickstart(FibonacciService())
