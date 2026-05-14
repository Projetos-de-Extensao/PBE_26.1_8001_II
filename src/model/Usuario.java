package model;

public class Usuario {

    private int id;
    private String nome;
    private String email;
    private String senha;
    private StatusUsuario perfil; 

   
    public Usuario() {}

    
    public Usuario(int id, String nome, String email, String senha, StatusUsuario perfil) {
        this.id = id;
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.perfil = perfil;
    }

    

    
    public void login() {
        System.out.println("Usuário " + nome + " entrou no sistema.");
    }

    
    public void logout() {
        System.out.println("Usuário " + nome + " saiu do sistema.");
    }

    
    public void recuperarSenha() {
        System.out.println("E-mail de recuperação enviado para: " + email);
    }

    

    public int getId() { return id; }
    public void setId(int id) { this.id = id; }

    public String getNome() { return nome; }
    public void setNome(String nome) { this.nome = nome; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getSenha() { return senha; }
    public void setSenha(String senha) { this.senha = senha; }

    public StatusUsuario getPerfil() { return perfil; }
    public void setPerfil(StatusUsuario perfil) { this.perfil = perfil; }

    
    @Override
    public String toString() {
        return "Usuario{id=" + id + ", nome='" + nome + "', email='" + email + "', perfil=" + perfil + "}";
    }
}