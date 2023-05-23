from colour import Color
from manim import *
from manim_presentation import Slide
from PIL import Image
import math
import numpy as np

class Beamer(Slide,ThreeDScene):
    def construct(self):
        self.wait()
        BeamerTitle.construct(self)
        BeamerIntro.construct(self)
        BeamerQubits.construct(self)
        BeamerQubitGates.construct(self)
        BeamerQubitCircuits.construct(self)
        BeamerQubitPauli.construct(self)
        BeamerQubitDotSigma.construct(self)
        BeamerQubitExp.construct(self)
        BeamerMatrixMultiplication.construct(self)
        BeamerSpaceTimeAlgebra.construct(self)
        BeamerQudits.construct(self)
        BeamerQuditGates.construct(self)
        BeamerQuditGenerators.construct(self)
        BeamerNoncommutativeTorus.construct(self)
        BeamerConlusion.construct(self)
        BeamerReferences.construct(self)
        self.wait()

class BeamerTitle(Slide):  
    def construct(self):
        self.clear()
        title = Title("Qudit Gates and Noncommutative Tori",match_underline_width_to_text=True).scale(1.2).next_to(ORIGIN,direction=UP)
        author = Tex("\\centering{Carlos Efrain Quintero Narvaez \\\\ efrainq07@ciencias.unam.mx}").scale(0.8).next_to(ORIGIN,direction=DOWN)
        school = Tex("Universidad Nacional Autónoma de México \\\\\ Facultad de Ciencias").scale(0.5).to_edge(DOWN)
        self.wait()
        self.pause()
        self.play(Write(title))
        self.play(Write(author))
        self.play(Write(school))
        self.wait()
        self.pause()

class BeamerIntro(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line0 = Tex(r"""\justifying{
        This presentation shows results from the 2000 paper\\
        by Alexander Yu. Vlasov:\\
        ''Noncommutative tori and universal sets of non-binary\\
        quantum gates''\\
        There it is shown how to use the structure of the\\
        noncommutative torus to do calculations for non-binary\\
        quantum systems in the context of universality.}
        """).to_corner(UL)

        line1 = Tex("\\justifying{Before proceeding any further let us do a brief\\\\ introduction to \\textbf{Quantum Computation}.}").next_to(line0,direction=DOWN).to_edge(LEFT).shift(DOWN*0.5)
        line2 = Tex("Specifically to the concept of the \\textbf{qubit}.")
        line2.next_to(line1,direction=DOWN).to_edge(LEFT).shift(DOWN*0.5)

        self.play(Write(line0))
        self.wait()
        self.pause()

        self.play(Write(line1))
        self.wait()
        self.pause()

        self.play(Write(line2))
        self.wait()
        self.pause()

        self.play(
            Unwrite(line1),
            Unwrite(line2),
            Unwrite(line0)
        )

class BeamerQubits(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex("Consider the classical case of bits and imagine a light bulb.").to_corner(UL)

        self.play(Write(line1))
        self.wait()
        self.pause()


        on_file ="images/light-on.png"
        off_file = "images/light-off.png"

        
        off_np_image = Image.open(off_file)
        off_image = ImageMobject(off_np_image)
        off_image.set_height(3)

        on_np_image = Image.open(on_file)
        on_image = ImageMobject(on_np_image)
        on_image.set_height(3)
        

        self.play(FadeIn(off_image))
        self.wait()
        self.pause()

        line2 = Tex("This light bulb can be \\textbf{on} and \\textbf{off}.").to_corner(UL)

        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

        self.remove(off_image)
        self.add(on_image)

        self.wait()
        self.pause()

        for i in range(6):
            self.remove(on_image)
            self.add(off_image)
            self.wait(duration=DEFAULT_WAIT_TIME*0.2)
            self.remove(off_image)
            self.add(on_image)
            self.wait(duration=DEFAULT_WAIT_TIME*0.2)

        self.wait()
        self.pause()

        line3 = Tex("\\justifying{This is represented in an abstract form by using a \\textbf{bit} \\\\ which can be a \\textbf{0} or a \\textbf{1}}").to_corner(UL)

        self.play(ReplacementTransform(line2,line3))
        self.wait()
        self.pause()

        bit0 = MathTex("0").next_to(off_image,direction=RIGHT).scale(2)
        bit1 = MathTex("1").next_to(on_image,direction=RIGHT).scale(2)

        self.play(Write(bit0))
        self.wait()
        self.pause()

        self.remove(off_image)
        self.remove(bit0)
        self.add(on_image)
        self.add(bit1)

        self.wait()
        self.pause()

        for i in range(6):
            self.remove(on_image)
            self.remove(bit1)
            self.add(off_image)
            self.add(bit0)
            self.wait(duration=DEFAULT_WAIT_TIME*0.2)
            self.remove(off_image)
            self.remove(bit0)
            self.add(on_image)
            self.add(bit1)
            self.wait(duration=DEFAULT_WAIT_TIME*0.2)

        self.remove(bit1)

        self.wait()
        self.pause()

        line4 = Tex("Now consider this light bulb case to be a \\textbf{quantum system}.").to_corner(UL)

        self.play(ReplacementTransform(line3,line4),Unwrite(bit0))       
        self.wait()
        self.pause()

        line5 = Tex("Thus we have two quantum \\textbf{basis states}.").to_corner(UL)
        off_ket_empty = MathTex("|\\quad\\rangle").scale(5)
        on_ket_empty = MathTex("|\\quad\\rangle").scale(5)

        off_ket = Group(off_ket_empty,off_image)
        on_ket = Group(on_ket_empty,on_image)

        self.play(ReplacementTransform(line4,line5))
        self.play(Write(off_ket_empty))
        self.add(on_ket_empty)
        self.play(
            ApplyMethod(off_ket.to_edge,LEFT),
            ApplyMethod(on_ket.to_edge,RIGHT)
            )
        self.wait()
        self.pause()

        line6 = Tex("Then we can consider \\textbf{linear superpositions} of these states.").to_corner(UL)

        superposition_empty = MathTex("\\alpha_0","|\\quad\\rangle","+","\\alpha_1","|\\quad\\rangle").scale(3)

        self.play(ReplacementTransform(line5,line6))
        self.play(
            ApplyMethod(off_ket.scale,0.6),
            ApplyMethod(on_ket.scale,0.6)
        )
        self.play(
            ApplyMethod(off_ket.move_to,superposition_empty[1]),
            ApplyMethod(on_ket.move_to,superposition_empty[-1])
        )
        self.play(Write(superposition_empty))
        self.wait()
        self.pause()

        line7 = Tex("which are each represented by $|0\\rangle$ and $|1\\rangle$.").to_corner(UL)
        superposition = MathTex("\\alpha_0","|0\\rangle","+","\\alpha_1","|1\\rangle").scale(3)

        self.play(
            ReplacementTransform(superposition_empty[0],superposition[0]),
            ReplacementTransform(superposition_empty[1],superposition[1]),
            ReplacementTransform(superposition_empty[2],superposition[2]),
            ReplacementTransform(superposition_empty[3],superposition[3]),
            ReplacementTransform(superposition_empty[-1],superposition[-1]),
            FadeOut(off_ket),
            FadeOut(on_ket),
            ReplacementTransform(line6,line7)
        )
        self.wait()
        self.pause()

        line8 = Tex("This what we call a \\textit{qubit}.").to_corner(UL)
        note1 = Tex("Note: See that $\\alpha_0,\\alpha_1 \\in \\mathbb{C}$ and $|\\alpha_0|^2+|\\alpha_1|^2=1$.").next_to(superposition,direction=DOWN)

        self.play(ReplacementTransform(line7,line8))
        self.play(Write(note1))
        self.wait()
        self.pause()

        line9 = Tex("The space of possible states for a qubit forms a\\\\ two dimensional complex Hilbert space denoted as $\\mathcal{H}(2)$").to_corner(UL)
        self.play(ReplacementTransform(line8,line9))
        self.wait()
        self.pause()


class BeamerQubitGates(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        \justifying{Now that we have seen what a \textbf{qubit} is\\
        we can consider how to do computations with them.}""")
        self.play(Write(line1))
        self.wait()
        self.pause()

        line2 = Tex(r"""
        \justifying{Recalling from the principles of quantum mechanics\\
        the transformations that can be done on a quantum system\\
        must always be \textbf{unitary}.}""")

        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

        line3 = Tex(r"""
        \justifying{Thus, we need to consider the group of\\
        unitary transformations on the state space of a qubit $\mathcal{H}(2)$\\
         which is denoted as $\mathrm{U}(2)$.}""")
        self.play(ReplacementTransform(line2,line3))
        self.wait()
        self.pause()

        line4 = Tex(r"""
        \justifying{A common representation of the group $\mathrm{U}(2)$ is\\
        as the group of unitary $2\times 2$ complex matrices:}""").to_corner(UL)
        matrix1 = MathTex(r"""
        U=
        \begin{pmatrix}
        u_{00} & u_{01}\\
        u_{10} & u_{11}
        \end{pmatrix}
        """).scale(2)
        matrix2 = MathTex(r"""\text{such that: }
        UU^{\dag} = U^{\dag}U = \mathbf{I}
        """).scale(2).next_to(matrix1,direction=DOWN)

        self.play(ReplacementTransform(line3,line4))
        self.play(Write(matrix1))
        self.play(Write(matrix2))
        self.wait()
        self.pause()


        

class BeamerQubitCircuits(Slide):

    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        \justifying{A common form of representing these gates\\
        is through the analog to classical logic circuits\\
        called \textbf{quantum circuits}.}
        """).to_corner(UL)
        self.play(Write(line1))
        self.wait()
        self.pause()

        diag1 = MathTex(r"""
        \Qcircuit @C=3em @R=.7em {
        & \gate{U} & \qw
        }""").scale(3)

        self.play(Write(diag1))
        self.wait()
        self.pause()

        line2 = Tex(r"""
        \justifying{
        The wire represents a qubit that flows from\\
        the right side and is acted upon by the\\
        unitary $U$ gate and continues to the left side.}
        """).to_corner(UL)
        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

        line3 = Tex(r"""
        \justifying{
        If we apply two gates $U_1,U_2\in\mathrm{U}(2)$ one after another\\
        we get the following circuit, where $U_1$ is applied first and then\\
        $U_2$ after that.}
        """).to_corner(UL)
        diag2 = MathTex(r"""
        \Qcircuit @C=3em @R=.7em {
        & \gate{U_1} & \gate{U_2} & \qw
        }""").scale(2)
        self.play(ReplacementTransform(line2,line3),ReplacementTransform(diag1,diag2))
        self.wait()
        self.pause()

class BeamerQubitPauli(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        \justifying{
        Moving on let us consider the following unitary\\
        matrices known as the \textbf{Pauli matrices}:
        }
        """).to_corner(UL)
        pauli_X = MathTex("X","=",r"""
        \begin{pmatrix}
        0 & 1\\
        1 & 0\\
        \end{pmatrix}""").next_to(line1,direction=DOWN)
        pauli_Y = MathTex("Y","=",r"""
        \begin{pmatrix}
        0 & -i\\
        i & 0
        \end{pmatrix}""").next_to(pauli_X,direction=DOWN)
        pauli_Z = MathTex("Z","=",r"""
        \begin{pmatrix}
        1 & 0\\
        0 & -1
        \end{pmatrix}
        """).next_to(pauli_Y,direction=DOWN)

        self.play(Write(line1))
        self.play(Write(pauli_X),Write(pauli_Y),Write(pauli_Z))
        self.wait()
        self.pause()

        line2 = Tex(r"""
        \justifying{
        These have the following properties:
        }
        """).to_corner(UL)

        X2 = MathTex("X^2","=","1").scale(2).next_to(line1,direction=DOWN).shift(DOWN+3*LEFT)
        Y2 = MathTex("Y^2","=","1").scale(2).next_to(X2,direction=DOWN)
        Z2 = MathTex("Z^2","=","1").scale(2).next_to(Y2,direction=DOWN)

        XY = MathTex("XY = -YX = iZ").scale(2).next_to(X2,direction=RIGHT).shift(RIGHT)
        YZ = MathTex("YZ = -ZY = iX").scale(2).next_to(Y2,direction=RIGHT).shift(RIGHT)
        ZX = MathTex("ZX = -XZ = iY").scale(2).next_to(Z2,direction=RIGHT).shift(RIGHT)

        self.play(ReplacementTransform(line1,line2))
        self.play(
            ReplacementTransform(pauli_X[0:2],X2[0:2]),
            ReplacementTransform(pauli_Y[0:2],Y2[0:2]),
            ReplacementTransform(pauli_Z[0:2],Z2[0:2]),
            Unwrite(pauli_X[2]),
            Unwrite(pauli_Y[2]),
            Unwrite(pauli_Z[2]),
            Write(X2[2]),
            Write(Y2[2]),
            Write(Z2[2]),
            Write(XY),
            Write(YZ),
            Write(ZX)
        )
        self.wait()
        self.pause()

class BeamerQubitDotSigma(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        \justifying{
        Thus, consider the following ''vector'' \\
        (which is actually just an abuse of notation).
        }
        """).to_corner(UL)

        self.play(Write(line1))
        self.wait()
        self.pause()

        sigma_vector = MathTex(r"\vec{\Sigma}","=",r"(","X",",","Y",",","Z",")").scale(2)
        self.play(Write(sigma_vector))
        self.wait()
        self.pause()

        line2 = Tex(r"""
        \justifying{
        Then consider a unit vector $\hat{n}$ in $\mathbb{R}^3$.
        }
        """).to_corner(UL)
        n_vector = MathTex(r"\hat{n}","=",r"(","n_x",",","n_y",",","n_z",")").scale(2).next_to(sigma_vector,direction=DOWN)

        self.play(ReplacementTransform(line1,line2))
        self.play(Write(n_vector))
        self.wait()
        self.pause()

        line3 = Tex(r"""
        \justifying{
        And finally, consider the dot product of these vectors\\
        (which is again an abuse of notation).\\
        This will result in another unitary matrix:
        }
        """).to_corner(UL)
        n_sigma = MathTex(r"\hat{n}",r"\cdot",r"\vec{\Sigma}","=",r"n_x","X", "+","n_y", "Y" ,"+","n_z","Z").scale(2)

        self.play(ReplacementTransform(line2,line3))
        self.play(
            ReplacementTransform(n_vector[0],n_sigma[0]),
            ReplacementTransform(sigma_vector[0],n_sigma[2]),
            ReplacementTransform(n_vector[3],n_sigma[4]),
            ReplacementTransform(sigma_vector[3],n_sigma[5]),
            ReplacementTransform(n_vector[5],n_sigma[7]),
            ReplacementTransform(sigma_vector[5],n_sigma[8]),
            ReplacementTransform(n_vector[7],n_sigma[10]),
            ReplacementTransform(sigma_vector[-2],n_sigma[-1]),
            Unwrite(n_vector[1]),
            Unwrite(n_vector[2]),
            Unwrite(n_vector[4]),
            Unwrite(n_vector[6]),
            Unwrite(n_vector[8]),
            Unwrite(sigma_vector[1]),
            Unwrite(sigma_vector[2]),
            Unwrite(sigma_vector[4]),
            Unwrite(sigma_vector[6]),
            Unwrite(sigma_vector[8]),
            )
        self.play(
            Write(n_sigma[1]),
            Write(n_sigma[3]),
            Write(n_sigma[6]),
            Write(n_sigma[9])
        )
        self.wait()
        self.pause()

        line4 = Tex(r"""
        \justifying{
        This matrix will have the following property:
        """).to_corner(UL)
        n_sigma2 = MathTex("(",r"\hat{n}",r"\cdot",r"\vec{\Sigma}",")^2",r"=","1").scale(2)
        
        self.play(ReplacementTransform(line3,line4))
        self.play(
            ReplacementTransform(n_sigma[0:3],n_sigma2[1:4]),
            Unwrite(n_sigma[3:]),
        )
        self.play(
            Write(n_sigma2[0]),
            Write(n_sigma2[4:]),
        )
        self.wait()
        self.pause()

        in_sigma2 = MathTex("(","i","(",r"\hat{n}",r"\cdot",r"\vec{\Sigma}",")",")^2",r"=","-","1").scale(2)

        line5 = Tex(r"""
        \justifying{
        And thus if we add an imaginary unit $i$ we get that $i(\hat{n}\cdot \vec{\Sigma})$\\
        can also act as an imaginary unit:
        """).to_corner(UL)
        self.play(ReplacementTransform(line4,line5))
        self.play(
            ReplacementTransform(n_sigma2[0],in_sigma2[0]),
            ReplacementTransform(n_sigma2[1:4],in_sigma2[3:6]),
            ReplacementTransform(n_sigma2[4],in_sigma2[7]),
            ReplacementTransform(n_sigma2[5],in_sigma2[-1]),
            ReplacementTransform(n_sigma2[6],in_sigma2[-3])
        )
        self.play(
            Write(in_sigma2[2]),
            Write(in_sigma2[1]),
            Write(in_sigma2[6]),
            Write(in_sigma2[-2])
        )
        self.wait()
        self.pause()

        line6 = Tex(r"""
        \justifying{
        This means that we can obtain a new version of Euler's\\
        identity as follows (this is done by inputting $\theta i(\hat{n}\cdot\vec{\Sigma})$\\
        with $\theta\in \mathbb{R}$ into the power series of the exponential).
        """).to_corner(UL)
        expi = MathTex(r"e^",r"{\theta",r"i(\hat{n}\cdot\vec{\Sigma})}","=",r"\cos\theta","+",r"i(\hat{n}\cdot\vec{\Sigma})",r"\sin\theta").scale(2)
        expipar = in_sigma2[1:7].copy()
        self.add(expipar)

        self.play(ReplacementTransform(line5,line6))
        self.play(
            ReplacementTransform(expipar,expi[-2]),
            ReplacementTransform(in_sigma2[1:7],expi[2]),
            Unwrite(in_sigma2[7:]),
            Unwrite(in_sigma2[0])
        )
        self.play(
            Write(expi[3:-2]),
            Write(expi[-1]),
            Write(expi[0:2])
        )
        self.wait()
        self.pause()

class BeamerQubitExp(Slide):
    def construct(self):
        
        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(
            r"""
            \justifying{
                Now, it is a known result that any unitary matrix in $U\in\mathrm{U}(2)$\\
                can be expressed as follows:
            }
            """
        ).to_corner(UL)
        expU = MathTex(r"U = e^{i\phi}",r"e^{i\theta (\hat{n}\cdot \vec{\Sigma})}").scale(2)
        tp = MathTex(r"\theta,\phi\in \mathbb{R}").scale(2).next_to(expU,direction=DOWN)

        self.play(Write(line1))
        self.play(Write(expU))
        self.play(Write(tp))
        self.wait()
        self.pause()

        expUext = MathTex(r"U = e^{i\phi}",r"(\cos\theta + i(\hat{n}\cdot\vec{\Sigma})\sin\theta)").scale(2)

        self.play(
            ReplacementTransform(expU[0],expUext[0]),
            ReplacementTransform(expU[1],expUext[1]),
            ApplyMethod(tp.next_to,expUext,{"direction":DOWN})
        )
        self.wait()
        self.pause()

        line2 = Tex(
            r"""
            \justifying{
               This will be useful in the following arguments.
            }
            """
        ).to_corner(UL)
        
        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

class BeamerMatrixMultiplication(Slide):
    def construct(self):
        
        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        It has now become clear that quantum computation uses\\
        matrices heavily.
        """)
        self.play(Write(line1))
        self.wait()
        self.pause()

        line2 = Tex(r"""
        However, take a look at the following matrix multiplication\\
        that is usually done in this context:
        """)

        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

        matmul1 = MathTex(r"""
        \begin{pmatrix}
        a_0 + i b_0 & a_1 + ib_1\\
        \\
        a_2 + i b_2 & a_3 + ib_3
        \end{pmatrix}
        """)
        matmul2 = MathTex(r"""
        \begin{pmatrix}
        a_0 + i b_0 & a_1 + ib_1\\
        \\
        a_2 + i b_2 & a_3 + ib_3
        \end{pmatrix}""",r"""\begin{pmatrix}
        u_0 + i v_0 & u_1 + iv_1\\
        \\
        u_2 + i v_2 & u_3 + iv_3
        \end{pmatrix}
        """)

        self.play(
            ApplyMethod(line2.to_corner,UL)
        )
        self.play(
            Write(matmul1)
        )
        self.play(
            ReplacementTransform(matmul1[0],matmul2[0]),
        )
        self.play(Write(matmul2[1]))
        self.wait()
        self.pause()

        matmul3 = MathTex(r"""\begin{pmatrix}
        (a_0 + i b_0)(u_0 + i v_0)+(a_1 + ib_1)(u_2 + i v_2 ) & (a_0 + i b_0)(u_1 + i v_1)+(a_1 + ib_1)(u_3 + i v_3 )\\
        \\
        (a_2 + i b_2)(u_0 + i v_0)+(a_3 + ib_3)(u_2 + i v_2 ) &  (a_2 + i b_2)(u_1 + i v_1)+(a_3 + ib_3)(u_3 + i v_3)
        \end{pmatrix}""").scale(0.6)

        self.play(Unwrite(matmul2))
        self.play(Write(matmul3))
        self.wait()
        self.pause()

        line3 =Tex(r"""
        As you can see, this quickly gets out of hand\\
        as we get quite a lot of arithmetic operations!
        """).to_edge(UP)
        self.play(
            ReplacementTransform(line2,line3)
        )
        self.wait()
        self.pause()

class BeamerSpaceTimeAlgebra(Slide):
    def construct(self):
        
        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        \justifying{
            Manipulation of quantum gates can be simplified by choosing\\
            a different representation of the unitary group $\mathrm{U}(2)$.\\
        }
        """).shift(UP*2)
        line2 = Tex(r"""
        \justifying{
           Specifically that of \textbf{Clifford Algebras} which in this context\\
            is known as the \textbf{Space-Time Algebra}. 
        }
        """).next_to(line1,direction=DOWN)

        self.play(Write(line1))
        self.wait()
        self.pause()

        self.play(Write(line2))
        self.wait()
        self.pause()

        line3 = Tex(r"""
        \justifying{
           For this, consider an algebra generated by three elements\\
           $\sigma_1,\sigma_2,\sigma_3$ and an identity $1$.\\
            With a bilinear product with the following rules:
        }
        """).to_corner(UL)

        units = MathTex(r"""
        &\sigma_1\sigma_2\sigma_3 = i & i^2=-1\\
        &(\sigma_1)^2=1  &\sigma_1\sigma_2 =-\sigma_2\sigma_1 = i\sigma_3\\
        &(\sigma_2)^2=1  &\sigma_2\sigma_3 = -\sigma_3\sigma_2 = i\sigma_1\\
        &(\sigma_3)^2=1  &\sigma_3\sigma_1 = -\sigma_1\sigma_3 = i\sigma_2\\
        """)

        self.play(
            Unwrite(line1),
            Unwrite(line2)
            )
        self.play(
            Write(line3)
        )
        self.play(
            Write(units)
        )
        self.wait()
        self.pause()

        self.play(
            Unwrite(units),
            Unwrite(line3)
        )

        line4 = Tex(r"""
        See then that if we consider a linear combination as follows:
        """).to_corner(UL)
        n1 = MathTex(r"n = n_1 \sigma_1 + n_2 \sigma_2 + n_3\sigma_3").scale(2)
        n2 = MathTex(r"n_1,n_2,n_3\in \mathbb{R} \quad n_1^2+n_2^2+n_3^2 = 1").scale(1.5).next_to(n1,direction=DOWN)

        self.play(
            Write(line4)
        )
        self.play(
            Write(n1),
            Write(n2)
        )
        self.wait()
        self.pause()

        line5 = Tex(r"""\justifying{
        This object has the following property analogous \\to that of $(\hat{n}\cdot\vec{\Sigma})$:
        }
        """).to_corner(UL)
        n3 = MathTex(r"n^2 = 1").scale(2)

        self.play(
            ReplacementTransform(line4,line5)
        )
        self.play(
            Unwrite(n1),
            Unwrite(n2)
            )
        self.play(
            Write(n3)
        )
        self.wait()
        self.pause()

        line6 = Tex(r"""\justifying{
        This in turn tells us that $in$ can work as an \\imaginary unit same as $i(\hat{n}\cdot\vec{\Sigma})$:
        }""").to_corner(UL)
        in1 = MathTex(r"(in)^2 = -1").scale(2).next_to(n3,direction=DOWN)

        self.play(
            ReplacementTransform(line5,line6)
        )
        self.play(Write(in1))
        self.wait()
        self.pause()

        line7 = Tex(r"""
        This allows us to find a version of Euler's identity:
        """).to_corner(UL)
        ein = MathTex(r"e^{in\theta} = \cos\theta + in \sin\theta").scale(2)

        self.play(ReplacementTransform(line6,line7))
        self.play(Unwrite(n3),Unwrite(in1))
        self.play(Write(ein))
        self.wait()
        self.pause()

        line8 = Tex(r"""\justifying{
        Same way as we did with matrices, we can represent any\\
        member of the unitary group $U\in \mathrm{U}(2)$ with\\
        the following object:}
        """).to_corner(UL)
        Ru = MathTex(r"""
        R_U = e^{i\phi} e^{in\theta}
        """).scale(2)
        Ru2 = MathTex(r"""
        R_U = e^{i\phi} (\cos\theta + in \sin\theta)
        """).scale(2)

        self.play(Unwrite(line7))
        self.play(Unwrite(ein))
        self.play(Write(line8))
        self.play(Write(Ru))
        self.play(ReplacementTransform(Ru,Ru2))
        self.wait()
        self.pause()

        line9 = Tex(r"""\justifying{
        This form of representing quantum gates simplifies \\
        calculations as we forget about the matrix nature of \\
        each element and replace it with a series of product\\
        relations.\\
        This is one of the advantages of the formalism\\
        of \textbf{Space-Time Algebras}.}
        """)
        
        self.play(Unwrite(line8),Unwrite(Ru2))
        self.play(Write(line9))
        self.wait()
        self.pause()

class BeamerQudits(Slide):
    def construct(self):
        
        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""\justifying{
        We have presented the framework\\
        of the qubit for quantum computation along\\
        with the algebraic representation of their gates\\
        with the \textbf{Space-Time Algebras}.
        }""")
        self.play(Write(line1))
        self.wait()
        self.pause()

        line2 = Tex(r"""\justifying{
        Now we'll present a different framework\\
        for quantum computation that generalizes\\
        the qubit.
        }""")
        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

        line3 = Tex(r"""\justifying{
        For this, remember our analogy\\
        with the light bulb:
        }""").to_corner(UL)
        self.play(Unwrite(line2))
        self.play(Write(line3))
        self.wait()
        self.pause()

        on_file ="images/light-on.png"
        off_file = "images/light-off.png"

        
        off_np_image = Image.open(off_file)
        off_image = ImageMobject(off_np_image)
        off_image.set_height(3)

        on_np_image = Image.open(on_file)
        on_image = ImageMobject(on_np_image)
        on_image.set_height(3)
        colors = [RED,GREEN,BLUE,PINK,ORANGE,PURPLE]
        color_images = [ on_image.copy().set_color(coloring) for coloring in colors]

        self.play(FadeIn(off_image))
        for i in range(6):
            self.remove(off_image)
            self.add(on_image)
            self.wait(duration=DEFAULT_WAIT_TIME*0.2)
            self.remove(on_image)
            self.add(off_image)
            self.wait(duration=DEFAULT_WAIT_TIME*0.2)
        self.wait()
        self.pause()

        line4 = Tex(r"""\justifying{
        However this time consider that the light bulb can turn on\\
        with a number $d-1$ of different colors.\\
        Giving it a total of $d$ possible states.
        }""").to_corner(UL)

        self.play(ReplacementTransform(line3,line4))
        self.wait()
        self.pause()

        past_image = off_image
        for image in color_images:
            self.remove(past_image)
            self.add(image)
            self.wait(duration=DEFAULT_WAIT_TIME*0.4)
            past_image = image
        self.remove(past_image)
        self.add(off_image)
        self.wait()
        self.pause()

        line5 = Tex(r"""\justifying{
        We can represent each of this states with a number\\
        in $\{0,1,\hdots,d-1\}$.
        }""").to_corner(UL)
        digits = [MathTex(str(count+1)).next_to(off_image,direction=RIGHT).scale(2) for count,value in enumerate(colors)]
        off_digit = MathTex("0").next_to(off_image,direction=RIGHT).scale(2)
        self.play(ReplacementTransform(line4,line5))
        self.play(Write(off_digit))
        self.wait()
        self.pause()

        past_digit = off_digit
        for image,digit in zip(color_images,digits):
            self.remove(past_digit)
            self.add(image)
            self.add(digit)
            self.wait(duration=DEFAULT_WAIT_TIME*0.4)
            past_digit = digit
        self.wait()
        self.pause()
        off_ket_empty = MathTex("|\\quad\\rangle").scale(5)
        line6 = Tex(r"""\justifying{
        Now, we can consider this light bulb to be a\\
        \textbf{quantum system}. This way, each of these\\
        color states is an element of a \textbf{quantum basis}.
        }""").to_corner(UL)

        self.play(Unwrite(past_digit))
        self.play(ReplacementTransform(line5,line6))
        self.play(Write(off_ket_empty))
        self.wait()
        self.pause()
        
        off_ket = Group(off_ket_empty,off_image)
        image_kets = [Group(off_ket_empty.copy(),image) for image in color_images]

        for image_ket in image_kets:
            self.add(image_ket)

        qudit1 = MathTex(r"\alpha_0",r"|\quad\rangle","+",r"\alpha_1",r"|\quad\rangle","+",r"\alpha_2",r"|\quad\rangle","+",r"\alpha_3",r"|\quad\rangle",
        "+",r"\alpha_4",r"|\quad\rangle","+",r"\alpha_5",r"|\quad\rangle","+",r"\alpha_6",r"|\quad\rangle").scale(0.8)

        line7 = Tex(r"""\justifying{
        Thus, we can consider \textbf{linear superpositions} of these\\
        quantum basis states:
        }""").to_corner(UL)

        self.play(ReplacementTransform(line6,line7))
        self.play(
            ApplyMethod(off_ket.scale,0.2*0.8),
            *[ApplyMethod(image_ket.scale,0.2*0.8) for image_ket in image_kets]
            )
        self.play(
            ApplyMethod(off_ket.move_to,qudit1[1]),
            *[ApplyMethod(image_ket.move_to,qudit1[3*(count+1)+1]) for count,image_ket in enumerate(image_kets)]
        )
        self.play(Write(qudit1))
        self.wait()
        self.pause()

        line8 = Tex(r"""\justifying{
        These quantum states can also be represented by numbers\\
        as follows:
        }""").to_corner(UL)

        self.play(ReplacementTransform(line7,line8))
        self.wait()
        self.pause()

        qudit2 = MathTex(r"\alpha_0",r"|0\rangle","+",r"\alpha_1",r"|1\rangle","+",r"\alpha_2",r"|2\rangle","+",r"\alpha_3",r"|3\rangle",
        "+",r"\alpha_4",r"|4\rangle","+",r"\alpha_5",r"|5\rangle","+",r"\alpha_6",r"|6\rangle").scale(0.8)

        self.play(
            ReplacementTransform(qudit1,qudit2),
            FadeOut(off_ket),
            *[FadeOut(image_ket) for image_ket in image_kets]
            )
        self.wait()
        self.pause()

        qudit3 = MathTex(r"\alpha_0",r"|0\rangle","+",r"\alpha_1",r"|1\rangle","+",r"\alpha_2",r"|2\rangle","+",r"\hdots","+",r"\alpha_{d-1}",r"|d-1\rangle")

        self.play(
            ReplacementTransform(qudit2[0:9],qudit3[0:9]),
            ReplacementTransform(qudit2[9:-3],qudit3[9:-3]),
            ReplacementTransform(qudit2[-3:],qudit3[-3:])
            )
        self.wait()
        self.pause()

        line9 = Tex(r"""\justifying{
        This object is called a \textbf{qudit} referencing that\\
        it has $d$ states. Analogously to qubits these objects\\
        state space is a $d$-dimensional complex Hilbert space\\
        denoted as $\mathcal{H}(d).$
        }""").to_corner(UL)

        self.play(
            ReplacementTransform(line8,line9)
        )
        self.wait()
        self.pause()

        note1 = Tex(r"""\justifying{
        Note: $\alpha_1,\hdots,\alpha_{d-1}\in \mathbb{C}$ and $|\alpha_1|^2+\hdots+|\alpha_{d-1}|^2=1$
        }""").next_to(qudit3,direction=DOWN)
        self.play(Write(note1))
        self.wait()
        self.pause()

class BeamerQuditGates(Slide):
    def construct(self):
        
        self.clear()
        self.wait()
        self.pause()     

        line1 = Tex(r"""
        \justifying{
            Now that we have generalized the concept of a\\
            qubit by defining qudits, we must consider how\\
            to manipulate this objects in order to do\\
            computations with them.
        }
        """)

        self.play(Write(line1))
        self.wait()
        self.pause() 

        line2 = Tex(r"""
        \justifying{
            As said before, the principles of quantum\\
            mechanics dictate that any transformation\\
            done onto a quantum system must be \textbf{unitary}.
        }
        """)

        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause() 

        line3 = Tex(r"""
        \justifying{
            Thus, we must consider the group of unitary\\
            transformations on $\mathcal{H}(d)$ which\\
            is denoted as $\mathrm{U}(d)$.
        }
        """)

        self.play(ReplacementTransform(line2,line3))
        self.wait()
        self.pause()

        line4 = Tex(r"""
        \justifying{
            Again one common representation of $\mathrm{U}(d)$\\
            is done using the group of unitary $d\times d$\\
            complex matrices. For example:
        }
        """)
        self.play(ReplacementTransform(line3,line4))
        self.play(ApplyMethod(line4.to_corner,UL))
        self.wait()
        self.pause()

        Ugate = MathTex(r"""
        &U = \begin{pmatrix}
        u_{00} & \hdots & u_{0(d-1)}\\
        \vdots & \ddots & \vdots\\
        u_{(d-1)0} & \hdots & u_{(d-1)(d-1)}\
        \end{pmatrix}\\
        &\text{such that }UU^{\dag}=U^{\dag}U = \mathbf{I}
        """)

        self.play(Write(Ugate))
        self.wait()
        self.pause()
        
        line5 = Tex(r"""
        \justifying{
            Having this, let us consider two important\\
            qudit gates in $\mathrm{U}(d)$.
        }
        """).to_corner(UL)

        self.play(ReplacementTransform(line4,line5),Unwrite(Ugate))
        self.wait()
        self.pause()

        xdzd = MathTex("&X_d","=",r"""\begin{pmatrix}
        0 & 0 & \hdots & 0 & 1\\
    1 & 0 & \hdots & 0 & 0\\
    0 & 1 & \hdots & 0 & 0\\
    \vdots & \vdots & \ddots & \vdots & \vdots\\
    0 & 0 & \hdots & 1 & 0
        \end{pmatrix}""",
        " &Z_d","=",r"""\begin{pmatrix}
        1 & & & \\
        & e^{i\frac{2\pi}{d}} &  & \\
        & & \ddots &\\
        & & & e^{i\frac{2\pi (d-1)}{d}}
        \end{pmatrix}""")
        self.play(Write(xdzd))
        self.wait()
        self.pause()

        line6 = Tex(r"""
        \justifying{
            The action of these matrices is as follows:
        }
        """).to_corner(UL)

        self.play(ReplacementTransform(line5,line6))
        self.wait()
        self.pause()

        Xdaction = MathTex(r"X_d|k\rangle = |(k+1) \text{ mod } d\rangle")

        self.play(Unwrite(xdzd))
        self.play(Write(Xdaction))
        self.wait()
        self.pause()

        Zdaction = MathTex(r"Z_d|k\rangle = e^{i\frac{2\pi k}{d}}|k\rangle").next_to(Xdaction,direction=DOWN)

        self.play(Write(Zdaction))
        self.wait()
        self.pause()

        line7 = Tex(r"""
        \justifying{
            Also when multiplying these matrices between\\
            themselves we have the following properties:
        }
        """).to_corner(UL)
        xdzdcomm = MathTex(r"""
        (X_d)^d &= \mathbf{I}\\
        (Z_d)^d &= \mathbf{I}\\
        X_dZ_d &= e^{i\frac{2\pi}{d}}Z_d X_d
        """)

        self.play(ReplacementTransform(line6,line7),Unwrite(Xdaction),Unwrite(Zdaction))
        self.play(Write(xdzdcomm))
        self.wait()
        self.pause()


class BeamerQuditGenerators(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""\justifying{
        Now let us mention the known property that if we\\
        let $U=X_d$ and $V=Z_d$ and consider the set of\\
        elements of the form $U^nV^m$ as follows:}
        """)
        self.play(Write(line1))
        self.wait()
        self.pause() 

        basisUV = MathTex(r"""
        &U^0 V^0, U^1 V^0,\hdots, U^{d-1}V^0\\
        &U^0 V^1, U^1 V^1,\hdots, U^{d-1}V^1\\
        &\vdots\\
        &U^0 V^{d-1}, U^1 V^{d-1},\hdots, U^{d-1}V^{d-1}\\
        """)

        self.play(ApplyMethod(line1.to_corner,UL))
        self.play(Write(basisUV))
        self.wait()
        self.pause()

        line2 = Tex(r"""\justifying{
        Then we get a basis for $\mathrm{U}(d)$.\\
        This will be very useful as we will see next.}""").to_corner(UL)

        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

class BeamerNoncommutativeTorus(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""\justifying{
        Now that we have established some useful properties\\
        of qudit gates analogous to those of the Pauli\\
        matrices we mentioned for qubits, we face the same\\
        situation we did before:}
        """)

        self.play(Write(line1))
        self.wait()
        self.pause()

        line2 = Tex(r"""\justifying{
        Matrices are too hard to manipulate!\\
        More so now that we are dealing with arbitrary\\
        $d\times d$ matrices!}
        """)
        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

        line3 = Tex(r"""\justifying{
        For this we do the same as with the \textbf{Space-Time Algebra}:\\
        Forget about the matrix nature of our gates and define\\
        an algebra with the same relations between elements.\\}
        """)
        self.play(ReplacementTransform(line2,line3))
        self.wait()
        self.pause()

        line4 = Tex(r"""\justifying{
        For this we use the structure of the so called\\
        \textbf{Noncommutative Torus}.}
        """)
        self.play(ReplacementTransform(line3,line4))
        self.wait()
        self.pause()

        line5 = Tex(r"""\justifying{
        Thus, consider an algebra with two basic elements $T_x$ and $T_y$\\
        and an identity element $1$ with the following relations for\\
        their bilinear product:}""").to_corner(UL)
        self.play(ReplacementTransform(line4,line5))
        self.wait()
        self.pause()

        txtyprop = MathTex(r"""
        (T_x)^d &= 1\\
        (T_z)^d &= 1\\
        T_xT_z &= e^{i\frac{2\pi}{d}} T_zT_x
        """)
        self.play(Write(txtyprop))
        self.wait()
        self.pause()

        line6 = Tex(r"""\justifying{
            Then this algebra will have a basis given by:
        }""").to_corner(UL)

        self.play(ReplacementTransform(line5,line6))
        self.wait()
        self.pause()

        basisXY = MathTex(r"""
        &1, T_x,T_x^2,\hdots, T_x^{d-1}\\
        &T_z, T_xT_z,T_x^2 T_z,\hdots, T_x^{d-1}T_z\\
        &\vdots\\
        &T_z^{d-1}, T_x T_z^{d-1},T_x^2 T_z^{d-1},\hdots, T_x^{d-1} T_z^{d-1}\\
        """)

        self.play(Unwrite(txtyprop))
        self.play(Write(basisXY))
        self.wait()
        self.pause()

        line7 = Tex(r"""\justifying{
            Thus, seeing the similarities between $T_x, T_z$ and\\
            $X_d, Z_d$ we conclude that we can find an object on this\\
            algebra for any qudit gate using the basis shown below.
        }""").to_corner(UL)

        self.play(ReplacementTransform(line6,line7))
        self.wait()
        self.pause()

class BeamerConlusion(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""
        Therefore we have shown a way to extend the method\\
        used to simplify calculations for qubit gates with\\
        the \textbf{Space-Time Algebra} to the framework of\\
        qudits and qudit gates using the \textbf{Noncommutative Torus}.
        """)

        self.play(Write(line1))
        self.wait()
        self.pause()

        line2 = Tex(r"""
        This was shown for the first time in the 2000 article\\
        ''Noncommutative tori and universal sets of non-binary\\
        quantum gates''\\
        by the russian physicist Alexander Yu. Vlasov.
        """)

        self.play(ReplacementTransform(line1,line2))
        self.wait()
        self.pause()

class BeamerReferences(Slide):
    def construct(self):

        self.clear()
        self.wait()
        self.pause()

        line1 = Tex(r"""\justifying{
        References}
        """).scale(1.5).to_corner(UL)
        line2 = Tex(r"""\justifying{
        1. Alexander Yu. Vlasov , Noncommutative tori and\\
        universal sets of nonbinary quantum gates,\\
        J. Math. Phys. 43, 2959-2964 (2002)\\
        https://doi.org/10.1063/1.1476391\\ \\
        2. Doran, C., Lasenby, A. \& Gull, S. States and operators in\\
        the spacetime algebra. Found Phys 23, 1239-1264 (1993).\\
        https://doi.org/10.1007/BF01883678}""").to_edge(LEFT)

        self.play(Write(line1),Write(line2))
        self.wait()
        self.pause()