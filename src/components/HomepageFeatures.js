import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: '应用中心',
    Svg: require('../../static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        数百个应用的快速使用指南。
      </>
    ),
  },
  {
    title: '安装',
    Svg: require('../../static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        下载并将 Websoft9 安装到您的服务器。
      </>
    ),
  },
  {
    title: '技术支持',
    Svg: require('../../static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        订阅客户，随时联系我们的客户成功团队吧
      </>
    ),
  }


];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
