package project.investment.domain.attendance;

import lombok.Getter;

import javax.persistence.*;
import java.util.Date;

@Entity
@Getter
public class Attendance {

    @Id @GeneratedValue
    @Column(name = "attendance_id")
    private Long id;
    private Long user_id;
    private Date createdAt;
}
