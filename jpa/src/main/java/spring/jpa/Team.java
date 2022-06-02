package spring.jpa;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Getter @Setter
@Entity
public class Team {

    @Id
    @GeneratedValue
    @Column(name = "TEAM_ID")
    private Long id;

    private String name;

    @OneToMany
    @JoinColumn(name = "TEAM_ID")
    private List<Member> members = new ArrayList<Member>();

    public Team(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public void addMember(Member member) {
        this.members.add(member);
        if(member.getTeam() != this) {
            member.setTeam(this);
        }
    }
}
