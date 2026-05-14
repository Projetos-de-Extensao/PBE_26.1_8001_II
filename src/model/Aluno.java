package model;

public class Aluno extends Usuario {

    private String matricula;
    private String curso;

   
    public Aluno(int id, String nome, String email, String senha, String matricula, String curso) {
       
        super(id, nome, email, senha, StatusUsuario.ALUNO);
        this.matricula = matricula;
        this.curso = curso;
    }

    
    public void cadastrarEstagio(String nomeEmpresa) {
        System.out.println("Aluno " + getNome() + " cadastrou estágio na empresa: " + nomeEmpresa);
    }

   
    public String getMatricula() { return matricula; }
    public void setMatricula(String matricula) { this.matricula = matricula; }

    public String getCurso() { return curso; }
    public void setCurso(String curso) { this.curso = curso; }

    @Override
    public String toString() {
        return "Aluno{matricula='" + matricula + "', curso='" + curso + "', " + super.toString() + "}";
    }
}