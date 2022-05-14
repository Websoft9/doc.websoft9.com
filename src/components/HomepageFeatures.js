import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';
import Link from '@docusaurus/Link';

const FeatureList = [
  {
    title: '应用中心',
    url: '/docs/apps',
    Svg: require('../../static/img/undraw_apps.svg').default,
    description: (
      <>
        Websoft9 包含数百个应用启动包以及知识库
      </>
    ),
  },
  {
    title: '云安装',
    url: '/docs/install/cloud',
    Svg: require('../../static/img/undraw_server.svg').default,
    description: (
      <>
        在主流的公有云平台快速安装 Websoft9
      </>
    ),
  },
  {
    title: '技术支持',
    url: '/docs/helpdesk',
    Svg: require('../../static/img/undraw_helpdesk.svg').default,
    description: (
      <>
        企业订阅客户随时获得 Websoft9 客户成功团队支持
      </>
    ),
  }


];

function Feature({Svg, title, url, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <Link to={url}><h3>{title}</h3></Link>
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
