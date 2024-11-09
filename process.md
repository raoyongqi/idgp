将 CSV 文件和栅格数据结合

另一种方法是使用 Join 来将 CSV 中的标签信息与栅格数据相结合，然后进行符号化。

    将 CSV 文件转换为表格：
        在 Catalog 面板中，右键点击你的 CSV 文件，选择 Create Table（创建表格），并选择一个地理数据库来保存表格。

    加入表格（Join）：
        将包含分类标签的表格与栅格数据进行 Join。你需要确保 CSV 表格中的 Value 列与栅格数据中的分类值字段（通常是 VALUE）匹配。
        在 Contents 面板中，右键点击栅格图层，选择 Joins and Relates > Add Join。
        在弹出的对话框中选择你转换的 CSV 表格，并选择匹配的字段（即 CSV 表中的 Value 与栅格数据中的 VALUE 字段匹配）。

    符号化栅格数据：
        完成 Join 后，回到栅格图层的 Symbology 面板，在 Field 下拉菜单中，选择包含标签的字段（例如，通过 Join 创建的新字段，包含从 CSV 文件中的标签信息）。
        选择 Unique Values 符号化类型并按照需要设置标签和颜色。