from typing import Optional, Any, TypeVar, Type, cast

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Education:
    certificate: Optional[str]
    university: Optional[str]

    def __init__(self, certificate: Optional[str], university: Optional[str]) -> None:
        self.certificate = certificate
        self.university = university

    @staticmethod
    def from_dict(obj: Any) -> 'Education':
        assert isinstance(obj, dict)
        certificate = from_union([from_str, from_none], obj.get("certificate"))
        university = from_union([from_str, from_none], obj.get("university"))
        return Education(certificate, university)

    def to_dict(self) -> dict:
        result: dict = {}
        result["certificate"] = from_union([from_str, from_none], self.certificate)
        result["university"] = from_union([from_str, from_none], self.university)
        return result


class Marriage:
    children: Optional[int]
    married: Optional[bool]
    spouse_name: Optional[str]

    def __init__(self, children: Optional[int], married: Optional[bool], spouse_name: Optional[str]) -> None:
        self.children = children
        self.married = married
        self.spouse_name = spouse_name

    @staticmethod
    def from_dict(obj: Any) -> 'Marriage':
        assert isinstance(obj, dict)
        children = from_union([from_int, from_none], obj.get("children"))
        married = from_union([from_bool, from_none], obj.get("married"))
        spouse_name = from_union([from_str, from_none], obj.get("spouse_name"))
        return Marriage(children, married, spouse_name)

    def to_dict(self) -> dict:
        result: dict = {"children": from_union([from_int, from_none], self.children),
                        "married": from_union([from_bool, from_none], self.married),
                        "spouse_name": from_union([from_str, from_none], self.spouse_name)}
        return result


class OnlineInfo:
    email: Optional[str]
    ip_address: Optional[str]
    ipv6_address: Optional[str]
    password: Optional[str]
    password_md5: Optional[str]
    user_agent: Optional[str]
    username: Optional[str]

    def __init__(self, email: Optional[str], ip_address: Optional[str], ipv6_address: Optional[str],
                 password: Optional[str], password_md5: Optional[str], user_agent: Optional[str],
                 username: Optional[str]) -> None:
        self.email = email
        self.ip_address = ip_address
        self.ipv6_address = ipv6_address
        self.password = password
        self.password_md5 = password_md5
        self.user_agent = user_agent
        self.username = username

    @staticmethod
    def from_dict(obj: Any) -> 'OnlineInfo':
        assert isinstance(obj, dict)
        email = from_union([from_str, from_none], obj.get("email"))
        ip_address = from_union([from_str, from_none], obj.get("ip_address"))
        ipv6_address = from_union([from_str, from_none], obj.get("ipv6_address"))
        password = from_union([from_str, from_none], obj.get("password"))
        password_md5 = from_union([from_str, from_none], obj.get("password_md5"))
        user_agent = from_union([from_str, from_none], obj.get("user_agent"))
        username = from_union([from_str, from_none], obj.get("username"))
        return OnlineInfo(email, ip_address, ipv6_address, password, password_md5, user_agent, username)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_union([from_str, from_none], self.email)
        result["ip_address"] = from_union([from_str, from_none], self.ip_address)
        result["ipv6_address"] = from_union([from_str, from_none], self.ipv6_address)
        result["password"] = from_union([from_str, from_none], self.password)
        result["password_md5"] = from_union([from_str, from_none], self.password_md5)
        result["user_agent"] = from_union([from_str, from_none], self.user_agent)
        result["username"] = from_union([from_str, from_none], self.username)
        return result


class Personal:
    age: Optional[int]
    blood: Optional[str]
    born: None
    born_place: Optional[str]
    cellphone: Optional[str]
    city: Optional[str]
    country: Optional[str]
    eye_color: Optional[str]
    father_name: Optional[str]
    gender: Optional[str]
    height: Optional[str]
    last_name: Optional[str]
    name: Optional[str]
    national_code: Optional[str]
    profile: Optional[str]
    religion: Optional[str]
    system_id: Optional[str]
    weight: Optional[int]

    def __init__(self, age: Optional[int], blood: Optional[str], born: None, born_place: Optional[str],
                 cellphone: Optional[str], city: Optional[str], country: Optional[str], eye_color: Optional[str],
                 father_name: Optional[str], gender: Optional[str], height: Optional[str], last_name: Optional[str],
                 name: Optional[str], national_code: Optional[str], profile: Optional[str], religion: Optional[str],
                 system_id: Optional[str], weight: Optional[int]) -> None:
        self.age = age
        self.blood = blood
        self.born = born
        self.born_place = born_place
        self.cellphone = cellphone
        self.city = city
        self.country = country
        self.eye_color = eye_color
        self.father_name = father_name
        self.gender = gender
        self.height = height
        self.last_name = last_name
        self.name = name
        self.national_code = national_code
        self.profile = profile
        self.religion = religion
        self.system_id = system_id
        self.weight = weight

    @staticmethod
    def from_dict(obj: Any) -> 'Personal':
        assert isinstance(obj, dict)
        age = from_union([from_int, from_none], obj.get("age"))
        blood = from_union([from_str, from_none], obj.get("blood"))
        born = from_none(obj.get("born"))
        born_place = from_union([from_str, from_none], obj.get("born_place"))
        cellphone = from_union([from_str, from_none], obj.get("cellphone"))
        city = from_union([from_str, from_none], obj.get("city"))
        country = from_union([from_str, from_none], obj.get("country"))
        eye_color = from_union([from_str, from_none], obj.get("eye_color"))
        father_name = from_union([from_str, from_none], obj.get("father_name"))
        gender = from_union([from_str, from_none], obj.get("gender"))
        height = from_union([from_str, from_none], obj.get("height"))
        last_name = from_union([from_str, from_none], obj.get("last_name"))
        name = from_union([from_str, from_none], obj.get("name"))
        national_code = from_union([from_str, from_none], obj.get("national_code"))
        profile = from_union([from_str, from_none], obj.get("profile"))
        religion = from_union([from_str, from_none], obj.get("religion"))
        system_id = from_union([from_str, from_none], obj.get("system_id"))
        weight = from_union([from_int, from_none], obj.get("weight"))
        return Personal(age, blood, born, born_place, cellphone, city, country, eye_color, father_name, gender, height,
                        last_name, name, national_code, profile, religion, system_id, weight)

    def to_dict(self) -> dict:
        result: dict = {"age": from_union([from_int, from_none], self.age),
                        "blood": from_union([from_str, from_none], self.blood), "born": from_none(self.born),
                        "born_place": from_union([from_str, from_none], self.born_place),
                        "cellphone": from_union([from_str, from_none], self.cellphone),
                        "city": from_union([from_str, from_none], self.city),
                        "country": from_union([from_str, from_none], self.country),
                        "eye_color": from_union([from_str, from_none], self.eye_color),
                        "father_name": from_union([from_str, from_none], self.father_name),
                        "gender": from_union([from_str, from_none], self.gender),
                        "height": from_union([from_str, from_none], self.height),
                        "last_name": from_union([from_str, from_none], self.last_name),
                        "name": from_union([from_str, from_none], self.name),
                        "national_code": from_union([from_str, from_none], self.national_code),
                        "profile": from_union([from_str, from_none], self.profile),
                        "religion": from_union([from_str, from_none], self.religion),
                        "system_id": from_union([from_str, from_none], self.system_id),
                        "weight": from_union([from_int, from_none], self.weight)}
        return result


class Work:
    country_code: Optional[str]
    insurance: Optional[bool]
    position: Optional[str]
    salary: Optional[str]

    def __init__(self, country_code: Optional[str], insurance: Optional[bool], position: Optional[str],
                 salary: Optional[str]) -> None:
        self.country_code = country_code
        self.insurance = insurance
        self.position = position
        self.salary = salary

    @staticmethod
    def from_dict(obj: Any) -> 'Work':
        assert isinstance(obj, dict)
        country_code = from_union([from_str, from_none], obj.get("country_code"))
        insurance = from_union([from_bool, from_none], obj.get("insurance"))
        position = from_union([from_str, from_none], obj.get("position"))
        salary = from_union([from_str, from_none], obj.get("salary"))
        return Work(country_code, insurance, position, salary)

    def to_dict(self) -> dict:
        result: dict = {"country_code": from_union([from_str, from_none], self.country_code),
                        "insurance": from_union([from_bool, from_none], self.insurance),
                        "position": from_union([from_str, from_none], self.position),
                        "salary": from_union([from_str, from_none], self.salary)}
        return result


class Person:
    education: Optional[Education]
    marriage: Optional[Marriage]
    online_info: Optional[OnlineInfo]
    personal: Optional[Personal]
    work: Optional[Work]

    def __init__(self, education: Optional[Education], marriage: Optional[Marriage], online_info: Optional[OnlineInfo],
                 personal: Optional[Personal], work: Optional[Work]) -> None:
        self.education = education
        self.marriage = marriage
        self.online_info = online_info
        self.personal = personal
        self.work = work

    @staticmethod
    def from_dict(obj: Any) -> 'Person':
        assert isinstance(obj, dict)
        education = from_union([Education.from_dict, from_none], obj.get("education"))
        marriage = from_union([Marriage.from_dict, from_none], obj.get("marriage"))
        online_info = from_union([OnlineInfo.from_dict, from_none], obj.get("online_info"))
        personal = from_union([Personal.from_dict, from_none], obj.get("personal"))
        work = from_union([Work.from_dict, from_none], obj.get("work"))
        return Person(education, marriage, online_info, personal, work)

    def to_dict(self) -> dict:
        result: dict = {"education": from_union([lambda x: to_class(Education, x), from_none], self.education),
                        "marriage": from_union([lambda x: to_class(Marriage, x), from_none], self.marriage),
                        "online_info": from_union([lambda x: to_class(OnlineInfo, x), from_none], self.online_info),
                        "personal": from_union([lambda x: to_class(Personal, x), from_none], self.personal),
                        "work": from_union([lambda x: to_class(Work, x), from_none], self.work)}
        return result


class Profile:
    person: Optional[Person]

    def __init__(self, person: Optional[Person]) -> None:
        self.person = person

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        person = from_union([Person.from_dict, from_none], obj.get("person"))
        return Profile(person)

    def to_dict(self) -> dict:
        result: dict = {"person": from_union([lambda x: to_class(Person, x), from_none], self.person)}
        return result


def profile_from_dict(s: Any) -> Profile:
    return Profile.from_dict(s)


def profile_to_dict(x: Profile) -> Any:
    return to_class(Profile, x)
