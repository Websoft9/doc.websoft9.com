/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import React, {type ReactNode} from 'react';
import Translate from '@docusaurus/Translate';
import Link from '@docusaurus/Link';

function WebsiteLink({to, children}: {to: string; children?: ReactNode}) {
  return (
    <Link to={to}>
      {children || (
        <Translate id="team.profile.websiteLinkLabel">website</Translate>
      )}
    </Link>
  );
}

interface ProfileProps {
  className?: string;
  name: string;
  children: ReactNode;
  githubUrl?: string;
  twitterUrl?: string;
}

function TeamProfileCard({
  className,
  name,
  children,
  githubUrl,
  twitterUrl,
}: ProfileProps) {
  return (
    <div className={className}>
      <div className="card card--full-height">
        <div className="card__header">
          <div className="avatar avatar--vertical">
            <img
              className="avatar__photo avatar__photo--xl"
              src={`${githubUrl}.png`}
              alt={`${name}'s avatar`}
            />
            <div className="avatar__intro">
              <h3 className="avatar__name">{name}</h3>
            </div>
          </div>
        </div>
        <div className="card__body">{children}</div>
        <div className="card__footer">
          <div className="button-group button-group--block">
            {githubUrl && (
              <a className="button button--secondary" href={githubUrl}>
                GitHub
              </a>
            )}
            {twitterUrl && (
              <a className="button button--secondary" href={twitterUrl}>
                Twitter
              </a>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

function TeamProfileCardCol(props: ProfileProps) {
  return (
    <TeamProfileCard {...props} className="col col--6 margin-bottom--lg" />
  );
}

export function ActiveTeamRow(): JSX.Element {
  return (
    <div className="row">
      <TeamProfileCardCol
        name="Xu Wei"
        githubUrl="https://github.com/qiaofeng1227">
        <Translate id="team.profile.Xu Wei.body">
          Websoft9 创始人之一，老黄牛。80 后码农 🤷‍♂️，写的代码与自己白头发一样多，但无怨无悔。
        </Translate>
      </TeamProfileCardCol>
      <TeamProfileCardCol
        name="Darren Chen"
        githubUrl="https://github.com/chendelin1982">
        <Translate id="team.profile.Darren Chen.body">
          Websoft9 创始人之一，资深企业软件行业从业者，云原生爱好者。虽然年龄在 35 岁以上，但仍然在努力贡献代码。
        </Translate>
      </TeamProfileCardCol>
      <TeamProfileCardCol
        name="Morning Tan"
        githubUrl="https://github.com/morning-tan">
        <Translate id="team.profile.Morning Tan.body">
          开源软件爱好者，本项目中主要从事测试工作。
        </Translate>
      </TeamProfileCardCol>
      <TeamProfileCardCol
        name="Lao Zhou"
        githubUrl="https://github.com/laozhou0731">
        <Translate id="team.profile.Lao Zhou.body">
          开源软件教育先行者，本项目中主要从事文档维护工作。
        </Translate>
      </TeamProfileCardCol>
    </div>
  );
}

export function ActiveArchitectRow(): JSX.Element {
  return (
    <div className="row">
      <TeamProfileCardCol
        name="Liu Guanghui"
        githubUrl="https://github.com/guanghui">
        <Translate id="team.profile.Liu Guanghui.body">
          资深架构师，曾在 OPPO 从事企业架构 20 年，经历完整的 ERP，MES，WMS，电商，OA等典型企业应用。
        </Translate>
      </TeamProfileCardCol>
    </div>
  );
}


export function HonoraryAlumniTeamRow(): JSX.Element {
  return (
    <div className="row">
      <TeamProfileCardCol
        name="Zengxc"
        githubUrl="https://github.com/zengxc-1996">
        <Translate id="team.profile.Zengxc.body">
          早起核心维护者之一，目前仍关注项目，并做出贡献🔥🔥🔥
        </Translate>
      </TeamProfileCardCol>
    </div>
  );
}

export function StudentFellowsTeamRow(): JSX.Element {
  return (
    <div className="row">
      <TeamProfileCardCol
        name="Brendan"
        githubUrl="https://github.com/dudeisbrendan03"
        twitterUrl="https://twitter.com/NameNotBrendan">
        <Translate
          id="team.profile.Brendan.body">
          Infra Engineer in Greater Manchester. Studying MSc @ Lancaster        </Translate>
      </TeamProfileCardCol>

      <TeamProfileCardCol
        name="Junhao"
        githubUrl="https://github.com/hnczhjh">
        <Translate id="team.profile.Junhao.body">
          RedHat Engineer CA, Studing at ChangSha colleage
        </Translate>
      </TeamProfileCardCol>

      <TeamProfileCardCol
        name="Biao Yang"
        githubUrl="https://github.com/hotHeart48156">
        <Translate id="team.profile.Biao Yang.body">
          Hot heart and smart developer
        </Translate>
      </TeamProfileCardCol>

      <TeamProfileCardCol
        name="QiuJiaHon"
        githubUrl="https://github.com/orgs/Websoft9/people/QiuJiaHon">
        <Translate id="team.profile.QiuJiaHon.body">
          Studing at Hunan Normal University
        </Translate>
      </TeamProfileCardCol>
    </div>
  );
}