package edu.smu.shop;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.SqlSessionTemplate;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import javax.sql.DataSource;

@SpringBootApplication
public class ShopApplication {

	public static void main(String[] args) {
		SpringApplication.run(ShopApplication.class, args);
	}
	@Bean
	public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception{
		SqlSessionFactoryBean sqlSessionFactory = new SqlSessionFactoryBean();
		sqlSessionFactory.setDataSource(dataSource);

		Resource[]resources =
				new PathMatchingResourcePatternResolver()
						.getResources("classpath:mappers/*.xml");
		sqlSessionFactory.setMapperLocations(resources);

		Resource configResource =
				new PathMatchingResourcePatternResolver()
						.getResource("classpath:config/mybatis-config.xml");
		sqlSessionFactory.setConfigLocation(configResource);

		return sqlSessionFactory.getObject();
	}
	@Bean
	public SqlSessionTemplate sqlSession(SqlSessionFactory sqlSessionFactory)throws Exception {
		return new SqlSessionTemplate(sqlSessionFactory);
	}
}
