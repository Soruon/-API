main_window = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>782</width>
    <height>558</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Карта</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="2" column="0">
     <layout class="QHBoxLayout" name="horizontalLayout_2">
      <item>
       <widget class="QLabel" name="label_2">
        <property name="text">
         <string>Вид карты:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="type1_btn">
        <property name="text">
         <string>Cхема</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="type2_btn">
        <property name="text">
         <string>Спутник</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="type3_btn">
        <property name="text">
         <string>Гибрид</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item row="0" column="0">
     <layout class="QHBoxLayout" name="horizontalLayout">
      <item>
       <widget class="QLabel" name="label">
        <property name="text">
         <string>Название места:</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QLineEdit" name="Place">
        <property name="placeholderText">
         <string>Место</string>
        </property>
       </widget>
      </item>
      <item>
       <widget class="QPushButton" name="Search_btn">
        <property name="text">
         <string>OK</string>
        </property>
       </widget>
      </item>
     </layout>
    </item>
    <item row="1" column="0">
     <widget class="QLabel" name="label_3">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''