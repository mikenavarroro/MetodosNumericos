import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class Principal extends JFrame implements ActionListener{

    private JButton biseccion, fPo, newton, pT, pP, pE, sec, salir;

    public Principal(){
        setLayout(null);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        getContentPane().setBackground(new Color(18, 18, 18));

        biseccion = new JButton("Metodo de Biseccion");
        biseccion.setBounds(320, 70, 200, 30);
        add(biseccion);
        biseccion.addActionListener(this);

        salir = new JButton("Salir");
        salir.setBounds(320, 450, 200, 30);
        add(salir);
        salir.addActionListener(this);

        fPo = new JButton("Metodo de Falsa Posicion");
        fPo.setBounds(320, 100, 200, 30);
        add(fPo);
        fPo.addActionListener(this);

        newton = new JButton("Metodo de Newton");
        newton.setBounds(320, 130, 200, 30);
        add(newton);
        newton.addActionListener(this);

        sec = new JButton("Metodo de la Secante");
        sec.setBounds(320, 160, 200, 30);
        add(sec);
        sec.addActionListener(this);

        pT = new JButton("Pivoteo Total");
        pT.setBounds(320, 190, 200, 30);
        add(pT);
        pT.addActionListener(this);

        pP = new JButton("Pivoteo Parcial");
        pP.setBounds(320, 220, 200, 30);
        add(pP);
        pP.addActionListener(this);

        pE = new JButton("Pivoteo Escalado");
        pE.setBounds(320, 250, 200, 30);
        add(pE);
        pE.addActionListener(this);
    }

    public void actionPerformed(ActionEvent e){
        if(e.getSource() == biseccion){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start Biseccion.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == fPo){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start FalsaPosicion.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == newton){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start Newton.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == sec){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start Secante.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == pT){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start PivoteoTotal.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == pP){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start PivoteoTotal.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == pE){
            Runtime app = Runtime.getRuntime();
            try{
            app.exec("cmd.exe /k start PivoteoTotal.py");
            }
            catch(Exception error){
                System.out.println("Error: " + error);
            }
        }

        if(e.getSource() == salir){
            System.exit(0);
        }
    }

    public static void main(String args[]){
        Principal ven = new Principal();
        ven.setBounds(0, 0, 800, 550);
        ven.setVisible(true);
        ven.setLocationRelativeTo(null);
        ven.setTitle("Metodos Numericos");
        ven.setResizable(false);
    }
}
