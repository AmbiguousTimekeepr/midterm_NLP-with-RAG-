import numpy as np
import pandas as pd

np.random.seed(42)

# Define question categories
question_types = [
    "Thông tin chung", "Chiến thuật", "Cầu thủ & Đội bóng", "Lịch sử", "Sự kiện & Giải đấu", "Phân tích trận đấu", "Huấn luyện viên", "Kỹ năng cá nhân", "Chiến thuật đội bóng", "Phong cách thi đấu", "Chuyển nhượng & Thị trường", "Cổ động viên & Văn hóa bóng đá", "Sự nghiệp cầu thủ", "Công nghệ trong bóng đá", "Ảnh hưởng xã hội của bóng đá"
]

# Sample keywords and topics for each category
question_keywords = {
    "Thông tin chung": ["bóng đá là gì", "luật việt vị", "VAR", "thời gian thi đấu", "trọng tài", "hệ thống giải đấu", "fair-play", "luật bàn thắng vàng", "luật thay người"],
    "Chiến thuật": ["phòng ngự phản công", "pressing", "tấn công trung lộ", "sơ đồ 4-3-3", "sơ đồ 5-3-2", "chiến thuật tiki-taka", "catenaccio", "gegenpressing", "bẫy việt vị"],
    "Cầu thủ & Đội bóng": ["Messi", "Ronaldo", "Erling Haaland", "Mbappe", "Real Madrid", "Barcelona", "Manchester United", "câu lạc bộ nhiều danh hiệu", "đội hình mạnh nhất"],
    "Lịch sử": ["World Cup đầu tiên", "Euro đầu tiên", "Champions League", "trận đấu nhiều bàn thắng nhất", "cầu thủ ghi nhiều bàn nhất", "sự ra đời luật việt vị", "Pele", "Maradona"],
    "Sự kiện & Giải đấu": ["Champions League", "Euro", "World Cup 2022", "Copa America", "Asian Cup", "V-League", "Premier League", "Bundesliga", "Serie A"],
    "Phân tích trận đấu": ["sơ đồ chiến thuật", "xG (expected goals)", "đánh giá cầu thủ", "thống kê chuyền bóng", "số lần dứt điểm", "tỷ lệ kiểm soát bóng", "phản công nhanh"],
    "Huấn luyện viên": ["Pep Guardiola", "Mourinho", "Sir Alex Ferguson", "Carlo Ancelotti", "chiến thuật huấn luyện viên", "vai trò của HLV trưởng", "HLV đội tuyển quốc gia"],
    "Kỹ năng cá nhân": ["sút bóng", "chuyền bóng", "kiểm soát bóng", "đánh đầu", "cách rê bóng", "cách sút phạt", "cách cản phá", "cách di chuyển không bóng"],
    "Chiến thuật đội bóng": ["tiki-taka", "gegenpressing", "catenaccio", "đội hình pressing", "tấn công tổng lực", "cách xây dựng đội hình", "vai trò của tiền vệ phòng ngự"],
    "Phong cách thi đấu": ["bóng đá đẹp", "bóng đá thực dụng", "bóng đá phòng ngự", "tấn công tổng lực", "bóng đá phản công nhanh", "bóng đá kiểm soát"],
    "Chuyển nhượng & Thị trường": ["thị trường chuyển nhượng", "các vụ chuyển nhượng đắt giá nhất", "luật chuyển nhượng FIFA", "cầu thủ tự do", "cách mua cầu thủ"],
    "Cổ động viên & Văn hóa bóng đá": ["Ultras", "hooligan", "bài hát cổ động", "sự cuồng nhiệt của fan", "cách cổ vũ đội bóng", "lễ hội bóng đá"],
    "Sự nghiệp cầu thủ": ["con đường trở thành cầu thủ chuyên nghiệp", "đào tạo cầu thủ trẻ", "giải nghệ", "chấn thương trong bóng đá", "hành trình của một cầu thủ"],
    "Công nghệ trong bóng đá": ["VAR", "goal-line technology", "phân tích dữ liệu cầu thủ", "thiết bị đo lường thể chất", "công nghệ làm bóng"],
    "Ảnh hưởng xã hội của bóng đá": ["bóng đá và chính trị", "tác động kinh tế của bóng đá", "các tổ chức bóng đá từ thiện", "bóng đá và bạo lực", "vai trò của bóng đá với cộng đồng"]
}

# Generate questions dataset
num_samples = 100000
question_corpus = []
for _ in range(num_samples):
    category = np.random.choice(question_types)
    keyword = np.random.choice(question_keywords.get(category, ["bóng đá"]))
    
    templates = {
        "Thông tin chung": [
            f"Bạn có thể giải thích {keyword} không?",
            f"{keyword} có vai trò gì trong bóng đá?",
            f"Luật {keyword} áp dụng như thế nào?",
            f"{keyword} ảnh hưởng thế nào đến trận đấu?",
            f"Làm thế nào để hiểu rõ hơn về {keyword}?"
        ],
        "Chiến thuật": [
            f"Chiến thuật {keyword} hoạt động ra sao?",
            f"{keyword} có hiệu quả không trong bóng đá hiện đại?",
            f"Đội nào áp dụng {keyword} thành công nhất?",
            f"Cách khắc chế chiến thuật {keyword} là gì?",
            f"Khi nào nên sử dụng {keyword} trong trận đấu?"
        ],
        "Cầu thủ & Đội bóng": [
            f"{keyword} có phải là cầu thủ vĩ đại nhất không?",
            f"Tại sao {keyword} được xem là đặc biệt?",
            f"{keyword} có đóng góp gì cho đội bóng của mình?",
            f"{keyword} có điểm mạnh và điểm yếu gì?",
            f"Cách chơi của {keyword} có ảnh hưởng đến bóng đá hiện đại không?"
        ],
        "Lịch sử": [
            f"Câu chuyện đằng sau {keyword} là gì?",
            f"Tại sao {keyword} là khoảnh khắc đáng nhớ?",
            f"{keyword} ảnh hưởng thế nào đến bóng đá hiện đại?",
            f"Những yếu tố nào dẫn đến {keyword}?",
            f"Hệ quả của {keyword} đối với lịch sử bóng đá là gì?"
        ],
        "Sự kiện & Giải đấu": [
            f"{keyword} có gì đặc biệt?",
            f"Giải đấu {keyword} có sức ảnh hưởng ra sao?",
            f"Tại sao {keyword} được nhiều người quan tâm?",
            f"Những cầu thủ xuất sắc nhất trong {keyword} là ai?",
            f"Làm thế nào để theo dõi {keyword} một cách tốt nhất?"
        ], 
        "Công nghệ trong bóng đá": [
            f"{keyword} giúp cải thiện trận đấu như thế nào?",
            f"Lợi ích và hạn chế của {keyword} là gì?",
            f"Công nghệ {keyword} hoạt động như thế nào?",
            f"Tại sao {keyword} gây tranh cãi?",
            f"Các giải đấu lớn sử dụng {keyword} ra sao?",
        ],
        "Phân tích trận đấu": [
        f"Làm thế nào để phân tích {keyword} trong trận đấu?",
        f"{keyword} ảnh hưởng thế nào đến kết quả trận đấu?",
        f"Các chỉ số quan trọng khi đánh giá {keyword} là gì?",
        f"Các đội bóng sử dụng {keyword} ra sao để giành chiến thắng?",
        f"Cách đọc dữ liệu {keyword} để hiểu rõ hơn trận đấu?"
        ],
        "Huấn luyện viên": [
            f"Tại sao {keyword} là một HLV xuất sắc?",
            f"Triết lý huấn luyện của {keyword} là gì?",
            f"{keyword} có ảnh hưởng thế nào đến đội bóng của mình?",
            f"Cách huấn luyện của {keyword} khác gì so với các HLV khác?",
            f"Các danh hiệu lớn nhất trong sự nghiệp của {keyword} là gì?"
        ],
        "Kỹ năng cá nhân": [
            f"Làm thế nào để cải thiện {keyword} trong bóng đá?",
            f"Những cầu thủ nào có {keyword} tốt nhất?",
            f"Tại sao {keyword} quan trọng đối với một cầu thủ?",
            f"Cách luyện tập để nâng cao {keyword} là gì?",
            f"{keyword} có thể tạo ra sự khác biệt trong trận đấu như thế nào?"
        ],
        "Chiến thuật đội bóng": [
            f"Làm thế nào để xây dựng {keyword} hiệu quả?",
            f"Các đội bóng hàng đầu áp dụng {keyword} như thế nào?",
            f"Tại sao {keyword} quan trọng trong bóng đá?",
            f"Cách khắc chế {keyword} của đối thủ?",
            f"Những yếu tố nào giúp {keyword} vận hành tốt nhất?"
        ],
        "Phong cách thi đấu": [
            f"Cách nhận biết phong cách {keyword} trong bóng đá?",
            f"Cầu thủ nào đại diện cho phong cách {keyword}?",
            f"Ưu và nhược điểm của phong cách {keyword} là gì?",
            f"Tại sao một số đội bóng chọn phong cách {keyword}?",
            f"{keyword} ảnh hưởng thế nào đến chiến thuật của đội bóng?"
        ],
        "Chuyển nhượng & Thị trường": [
            f"{keyword} có phải là thương vụ chuyển nhượng đáng chú ý?",
            f"Tại sao giá trị của {keyword} lại cao/thấp?",
            f"Các yếu tố quyết định thành công của {keyword} trong đội bóng mới?",
            f"Những thương vụ chuyển nhượng tương tự {keyword} trong quá khứ?",
            f"Cách các câu lạc bộ đánh giá cầu thủ trước khi mua {keyword}?"
        ],
        "Cổ động viên & Văn hóa bóng đá": [
            f"Lịch sử và ý nghĩa của {keyword} trong bóng đá?",
            f"{keyword} ảnh hưởng thế nào đến bầu không khí trận đấu?",
            f"Tại sao {keyword} quan trọng với người hâm mộ?",
            f"Những đội bóng nào nổi tiếng với {keyword}?",
            f"{keyword} có vai trò gì trong bản sắc của một CLB?"
        ],
        "Sự nghiệp cầu thủ": [
            f"Những cột mốc quan trọng trong sự nghiệp của {keyword}?",
            f"Tại sao {keyword} được xem là huyền thoại?",
            f"Sự nghiệp của {keyword} so với các cầu thủ khác thế nào?",
            f"Cách {keyword} phát triển từ cầu thủ trẻ thành ngôi sao?",
            f"Các danh hiệu quan trọng nhất trong sự nghiệp của {keyword}?"
        ],
        "Ảnh hưởng xã hội của bóng đá": [
            f"Bóng đá đã thay đổi {keyword} như thế nào?",
            f"{keyword} có tác động gì đến cộng đồng?",
            f"Tại sao bóng đá có thể giúp {keyword} phát triển?",
            f"Các dự án bóng đá nào đang giúp cải thiện {keyword}?",
            f"Lịch sử bóng đá đã chứng kiến ảnh hưởng của {keyword} ra sao?"
        ]
    }
    
    question = np.random.choice(templates.get(category, [f"Thông tin về {keyword}?"]))
    question_corpus.append((question, category))

# Save the generated dataset
output_df = pd.DataFrame(question_corpus, columns=["text", "label"])
output_file = "datasets/generated_soccer_questions.csv"
output_df.to_csv(output_file, index=False)

print(f"Dataset generated and saved to {output_file}")
