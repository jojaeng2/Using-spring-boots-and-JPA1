package spring.jpa;


import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Getter
@Entity
public class Member {

    @Id
    @GeneratedValue
    @Column(name = "MEMBER_ID")
    private Long id;
    private String username;

    @ManyToOne
    @JoinColumn(name = "TEAM_ID", insertable = false, updatable = false)
    private Team team;

    public Member(Long id, String username) {
        this.id = id;
        this.username = username;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setTeam(Team team) {
        this.team = team;
        if(!team.getMembers().contains(this)) {
            team.getMembers().add(this);
        }
    }
}