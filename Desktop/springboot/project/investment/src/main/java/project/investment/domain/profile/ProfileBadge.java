package project.investment.domain.profile;
import lombok.Getter;
import javax.persistence.*;

@Entity
@Getter
public class ProfileBadge {
    @Id @GeneratedValue
    @Column(name = "profile_badge_id")
    private Long id;
}
