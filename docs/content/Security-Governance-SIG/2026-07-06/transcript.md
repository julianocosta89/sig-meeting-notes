SIG: Security Governance SIG
Date: 2026-07-06
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Reiley 00:00:18 Hey, Charlie.
Charlie Eriksen 00:00:20 Hello?
Reiley 00:00:22 Hey, how are you doing?
Charlie Eriksen 00:00:23 I am good. How are you?
Reiley 00:00:26 Hey, good. Thank you for reaching out.
Charlie Eriksen 00:00:29 No problem.
Reiley 00:00:33 Okay, so… maybe I'll I can give you some quick contacts.
I'm not sure, like, how long have you been working on OpenTelemetry, or, like, OpenTelemetry is quite new So…
Charlie Eriksen 00:00:46 I mean, I'm familiar with OTEL, but like… I don't know anything about the organization whatsoever.
Reiley 00:00:54 Oh, okay, okay, so let me give you the context, and I think this meeting will probably just be two of us, and the meeting is automatically recorded. I think the video will be published on the OpenTelemetry channel on YouTube, so just letting you know.
So OpenTelemetry product started like seven years ago. So it used to be several products under the CNCF called Native Computation Foundation.
all of them are working on some part of the telemetry. And then OpenTelemetry came as a merger of two projects, OpenTracing and OpenCensus. So OpenTracing was more backed by startup companies, they got some adoption.
at that time, and OpenCensus was relatively new, but it was backed by a couple major enterprise companies, like Microsoft and Google, and instead of trying to, like, create the confusion, people start to wonder, like, which one should I use? Which one do I bet on? So folks decided, let's just merge the products, and… Initially, folks were focusing on distributed tracing, but as, like, people made progress, we start to add additional telemetry signals, and now we're, like, we have this goal of We want to give people one offer for all the telemetry signals, simply because we believe those telemetry signals are highly related, connected. For example, when people use distributed tracing, we think they will flow some like correlation ID across the distributed system. And then for all the logs, we want the logs to be also tagged with this distributed ID so we can connect it back.
When we send metrics, we also want metrics to be correlated. Anyway, so this is a product, and so far, I think we have, like, four telemetry signals, and as you probably see from the adoption, some of the languages are hugely successful used by Then on the other side, we're doomed because we're the eyes. And if people build software, they need to have the eyes to observe things. So we're affecting almost the entire software industry. Our security problem is becoming almost everyone's security problem.
Oh.
Speaking for myself, I joined the OpenTelemetry project on day one.
I'm employed by Microsoft.
and I used to work on one of the products before OpenTelemetry, so as a merger, you can imagine, I moved to OpenTelemetry. I worked on several projects until now, and I'm… I'm serving an OpenTelemetry technical community and also running the SIG security. So, to give you a little bit of context here, OpenTelemetry has two, like.
has the government's body under the CNCF, operational model. So we have the governance committee member who are elected by the community members. So, like, whoever made a contribution to OpenTelemetry that's considered non-trivial for the past one year.
will have the voting rights. Non-trivial means, like, if you just make a simple title fix or something, it's probably trivial, but if you make, like, 10 like, contributions, whether it's comment, issue, or fixing things, and consider it's, like, non-trivial. Then, they elect the governance committee members. So, governance committee members more like running the process, define the code of conduct, making sure the community is working. Then.
We have the initial list, and then later we got some internal election mechanism, but not public. And, that forms the… technical committee. So, technical committee members are more in charge of the technical direction, they review something like a product donation, and whether a product is reaching graduation or something. So, as part of the technical committee, you can imagine Well, we're expected to give people guidance and handle security problems. So as we're doing more, then at some point we realize the technical committee is spreading too thin. We don't want to have like 100 members there because otherwise like deciding something could be very hard, right? So we try to keep it under 10 folks.
And then, there are, like, specific projects, for example, like, how do we do this, packaging and bundling? The technical committee can decide to have, the special interesting groups taking care of that, and they try to delegate.
And of course, they're still accountable. So if things are falling apart, they will be accountable. For the SIG security, so the product started about like four years ago.
And we're trying to follow the model of the Kubernetes securities. We want people who have security background handling it. And ironically, I don't have a lot of security background. I've been a developer for very long time, so I work on low level stuff like compilers, debuggers.
and some of the telemetry, stuff. So, I started this, simply because, two reasons. One is, in OpenTelemetry, we see the security need.
And I do know people who want to help on security, so I try to, like, also help them so they can better contribute to the project. As a technical committee member.
I want this project to be successful, and I know that security is very important. Wearing another hat, I work for Microsoft, so Microsoft gives a lot of enterprise-level solution and product to critical customers, including some of the, like, the defense, military, whatever, like, very sensitive, I think, insurance, banking.
So, Microsoft cares about security, so I'm kind of, like, blessed by my company, saying, hey, like, we're trying to use OpenTelemetry in the product we give to our customers, so we do care about security.
spending time there, we're willing to pay you for that. So, I treat myself as a combination of the corporate interest and also the community interest, because I think this thing is very important. And… The city security has been.
like, riding a roller coaster, I was thinking previously. Like, initially, people were thinking, hey, like, we have some immediate problem, like, how do we sign the… the component? Like, we release some binary artifact, how do we digitally sign them?
And people are saying, oh, like, we should use the open source version, or people are saying we should use the corporate version, like, there's something. So we formed the security initially just to try to focus on that technical problem. Then after that got solved, we have other security issues. And you can imagine, like, we'll always have security issues.
And so, the problem is, people who wanted to solve that particular problem, they came, and they got some hat, like, they're the approver, project, like, leader or something. Then once they finish that, they're saying, okay, I'm done, I'm leaving. So, I'm the… one who's, like, I'm the only one who left as the current project lead to make sure this project won't die. And just to be transparent, I don't feel I have enough capacity to make a successful project here, so I definitely need help.
And so I have a selfish goal. I want to help you. I think you raise great points. And I also want to see if at some point maybe I can motivate you enough so you can help to drive something open to large. In return, you might get some open source reputation, things like that. So I'm willing to have that win-win situation.
the… the challenge I'm… I'm having is, number one, staffing, because a lot of people in open telemetry, they come either with a corporate, like, push, or they come with individual passion. So for individual passion, the problem I've seen is people really focus on the, like, performance, implementing features, those things. When it comes to, like, ice bomb, all the things, they say, no, like, not my problem. I'm just using that on my personal project, so I'm good enough, right? For the corporate one.
I think the problem is different companies, they have different bars, and for… For companies who have like, like very deep, involvement with banking, insurance, military defense, they, they.
they will be forced to have an extremely high bar. And then other companies start to say, okay, if you have a high bar, you're trying to lift the boat for us, then we don't have to do it. So there's constantly, like, an evaluation, how much energy we spend. So I… even on Microsoft, I feel like if someone else is willing to take more lead on security, my employer probably wants me to step back a little bit, so… so I'm more coming from, like, mainly driven by the community. As a technical committee member, I think this is important. I don't want this product to just ignore security.
Okay, so I hope that gives you the the contacts here, and we already had a couple email exchanges, so if possible, I still have to reach out to the Npm. Maintainers on open telemetry. See if they can also make it. But if it works, I want to invite you, and also folks on the Javascript and the broader seek to join the discussion, because I feel I'm more like the man in the middle, trying to relay the messages and adding some of my own judgment.
So I don't try to push people to the extreme, saying you have to be 100% secure, because there's no such definition, right? And even for simple things, like you're… like, I recommend you to use a corporate email. Then they don't have valid feedback. Some are saying, like.
in the repository management, if I put my corporate email, they don't even have a way for me to change my identity. So if I quit the company, I join another company.
then I have to abandon that account and use a different account. I cannot just change the email. So these are valid things. So my… my goal is I want to have a discussion, and this is more like a work-in-progress thing. I want us to document what's the understanding and our recommendation in OpenTelemetry. So for OpenTelemetry users, we kind of gave them the confidence by saying.
we do care about security, and these are the things we do, and also establish some pattern, because many projects, they don't have the influence like OpenTelemetry. Like, OpenTelemetry is one of the top projects in Under CNCF, in terms of the active contributors, it's probably, like, number one or number two. The Kubernetes… Probably is the number one.
So for such like a super active product and heavily used by almost everyone who need observability, I think setting some like best practice for security would also help the industry.
This is why I'm spending time on it. So hopefully it's still complex.
Okay, so I probably speak too much. Maybe I'll turn the mic to you.
Charlie Eriksen 00:12:05 Cool. So where should I start? I mean, I can, I can just summarize, right? Basically, right? Kind of the results quickly.
Right, so I… I've been looking at this whole maintainer hygiene thing, because after… It was like the ant V breeds by the North Koreans. I noticed like they had like dozens and dozens, right? Like, maintainers would write access to the package.
Yeah.
And when we also saw the compromise, sorry, AntV was not North Korea, that was the Mastra one. But Mastra, what was interesting was that they targeted a, I think it was X employee that still had valid credentials.
Reiley 00:12:50 Or even like XC Utils. I remember the XC Utils product with Mantenna.
And, like, an evil attacker trying to pretend to be an active maintainer for years, like, for two years.
Charlie Eriksen 00:13:05 Yep. Yeah, I mean, the reality is that there are threats out there that are quite persistent.
Right, even if it takes them a year to get into somewhere?
Right, that is well worth it.
Reiley 00:13:19 Yeah, if the value is high, and I think telemetry value is super high.
Charlie Eriksen 00:13:24 I mean, just looking, so I pulled all the data for the top 50,000 packages on NPM.
Right, and by scope, OpenTelemetry is number 1, 2, 3, 4, 5, 6.
But now that's better.
So that's quite significant.
For sure.
And generally what I've been seeing in the data is a combination of Right, and this is where it gets fussy, because a lot of packages belong to a certain corporation, right, that makes it really easy. And in that case, if you see what I call an ungoverned email address, right, so like a Gmail address on a corporate package, right, that's kind of… Makes no sense.
Reiley 00:14:07 Yeah, wearing my Microsoft hat, I totally agree with you. This is why when you see me interacting on GitHub and Slack, I use my corporate email address because I have the IT department supporting me. So I know if I'm on vacation, someone got access to my email, there are people who's going to take care of this for me.
Charlie Eriksen 00:14:24 Yep.
Exactly. The other thing I see a lot of is what I call, well, either ghost or dormant write grants. And it's basically people that have write access, but have never published a single package in the scope.
Right? It's like you have access, but you have never used it.
Reiley 00:14:46 Yes.
Charlie Eriksen 00:14:46 For that.
Reiley 00:14:47 That one already gave feedback to the NTM maintainers. I think they agree.
the principle is you only have permission if you really need to use that, right? It makes no sense for you to have the power, but not… it's just, like, increasing the attack surface for no benefit. So I think they're taking the action. For the email part.
like, some of them do have concerns, and I can share my observations. I, like, working in the open source, like, the open telemetry product for many years.
I kind of, like, got influenced by how things work. And I, like, you can tell, like, running the technical committee, driving some specification standard across many languages require me to like… I can still have strong opinion, but I have to absorb all the different perspectives and try to find a reasonable balance. So, it's probably, like, changed how my brain works, and I do have the empathy on both sides. So, currently, I would say I have some personal preference, but wearing my OpenTelemetry hats I, I, I think I'm still on the fence and yeah.
Let me share a couple of the things I've been thinking in the past two weeks after looking at your initial email.
So first, I think OpenTelemetry is trying to be an open source product in the public domain, like CNCF. So when we recruit people, I actually talk to the governance and technical committee members, share some of the ideas. So this is more like… I'm wearing my OpenTelemetry hat to express my thinking, but I think that also represents the thinking from several other members in OpenTelemetry. So the… the goal is we want… we want the project to be open for public contribution. We want… we want to tell the world, if you're willing to make the contribution, we'll welcome that. Instead, we try to say, if you're… trying to contribute. Well, check if you are employed by someone, or you're employed by a company that, like, many folks know. Like, we don't want to have this, like, perception of discrimination for whether people are employed or not, and what's their employer, or, like, which country are they coming from, but I can also, like, for example, if there's someone who talked to us, and they're saying, I'm coming from North Korea, and I'm, like, I'm building this parcel product, I want to contribute, I think it's very hard for us to say no, and we probably don't even want to say… we're not going to say, you come from a country where the Western world doesn't have a… like, you can look at me, I'm… I came from China, right? So… so we don't want to judge people by any of the… the… The identity, like the skin color, like the country they're coming from, the language they speak, so.
That's the core of open source, and we have that belief.
But on the other side, you can see we also want to have some level of trust. Like, if someone came and we've never seen them, we've never talked to them, they're making great contributions, then you can see there is a chance that they might be a hacker, like the XZTail situation. So we want to be able to have some input. For example, if someone reached out to me saying we have clear evidence that top contributor It's trying to put malicious code then, of course, I want to start the investigation with other members. So.
Like, you see, we do care about security, but we don't want to, like, have some discrimination there at all.
like the carve out a path is What I'm thinking, so we have to find out a reasonable path, but how do we do it? I think the trust in open source.
a lot of ways, like, you don't even see people in reality. You only, like, see maybe their icon. Someone will put on their icon, like a rabbit, or, like, I put something. If you don't talk, you don't even know if they're talking to a real person, or it's backed up by a group of hackers.
So that's my first challenge. So this principle, like how open source works versus we want security, seems to have some conflict. And I want to see what's your experience and advice for us.
Charlie Eriksen 00:19:12 Okay.
Okay, so one of the things I'm hearing, it is also this idea that open source into a very large extent, right, is a meritocracy, right? You're judged on what you bring to the community. You're trusted until you show that you cannot be trusted generally.
And I don't think, right, what I am, what I'm trying to kind of point out is that I don't think they are in conflict, really, because the… The thing is, like, you can contribute to a project without having write access on NPM.
Right, because, like, most of your pack.
Reiley 00:19:47 Oh, hello.
Charlie Eriksen 00:19:47 Trusted Publishing Right? So, the fact that, I mean… and… Right now, I mean, like, the… The packages, right, they're all being published, and the last time, like, most of them were published by a person was, like, 10 months ago.
So right now, most people don't even need to have ride access. Actually, just about zero.
Reiley 00:20:12 Yeah, so that part, I think, is quite clear, and the maintainers are taking the actions, so I already, like, gave them suggestions. I think we should have the folks who have never published anything, like, to have their personal accounts removed.
Yep. The second… still, I see the problem here, because we do have people who actually published the package recently, and they're saying.
I'm employed by a corporate, but I have to use my personal email address, because I learn… and here… here's what I learned in the past, and this is what I decided. And… and they do have a valid reason, and… It's hard for me to like like.
figure out, like, what's the best solution for that. Like, I know in Microsoft, when we try to hire some employee, we'll hire third-party companies to do the background survey, right? They'll tell whether you worked for some, like, you worked for some entity before that we believe is an enemy to the company or to the country or whatever, they will do this background check.
But in open source, when we have someone like you mentioned, it's purely based on their behavior.
during the engagement, so we don't have a chance to see anything else, like, besides the collaboration in OpenTelemetry. Like, after working on OpenTelemetry, if they work on something else, there's no way for us to know, except Except for the case where you might know some friend, and the friend knows them, right?
Charlie Eriksen 00:21:43 Yep.
I mean, I think.
I'm not too concerned about, like, personal email addresses, right? I don't think that's the biggest concern, right? The first thing you always want to do is reduce exposure.
And, yeah, it's always better, like.
I think for the individual, I think what I will say also is that Unfortunately, it's also a risk for them.
Right, so for instance, like last year, you remember when Deepak and Chalk got compromised?
The packages?
Reiley 00:22:16 I didn't know that.
Charlie Eriksen 00:22:17 Are you familiar with Debug and Chalk, the JavaScript packages?
Reiley 00:22:21 Oh.
Charlie Eriksen 00:22:22 So this guy, Just Junon, he's a really great guy. He used to be really big into the whole JavaScript ecosystem.
And he got phished, by the North Koreans.
And, I mean, he was responsible for a very significant portion of all packages by downloads on the NPM ecosystem.
I see. Yeah, like Wiz, Google's Wiz, based on their data, 99% of the cloud environments that they monitor had one of the packages that were compromised on the system.
99%.
Right. That's very lot exposure.
And I know from talking to him a bunch also afterwards, it was actually really traumatic for him to have to go through this experience of basically, right, people like trusting him, him getting compromised, right through a, you know, a very good phishing attack happening exactly at the right time where he was vulnerable as a person.
And I know he suffered quite a lot from it also in terms of mental health.
And I think that's a really big problem in open source. So what I would say is that, as an individual contributor.
You really want to limit your exposure, and, like, the more you can push it over to a corporate account.
the better.
But of course, again, it's really not my primary concern in this specific case. The primary concern is really reducing the attack surface, and in the cases where you do have, right, because your adoption is not 100% untrusted publishing, right, so what you really want to do in NPM is that you want to split up The packages, into different teams.
Reiley 00:24:02 Yeah, and avoid like one man have the ultimate power of almost everything. Yeah.
Charlie Eriksen 00:24:09 Exactly. What I would generally do is have one group for all packages that are using trusted publishing.
Right, because that one you can just reduce to basically no contributors at all.
Like, no maintenance.
And then, if you have… if you have individuals that are responsible for individual packages, like, a couple of packages that, like, one person is kind of… Running, or something like that. Create them a team for themselves.
So they can do non-trusted publishing deployments.
But you don't pool it all together.
Right, so you kind of give people their own little… Group.
Reiley 00:24:47 Yeah, you remind me of something. So maybe I'll tell you a quick story of what we did for OpenTelemetry.net. It's a collaboration with open source and Microsoft. So the problem is… OpenTelemetry.net packages used to be published by the OpenTelemetry GitHub pipelines. So you can imagine the source code is there, the maintainers are there, and they don't build the thing on their own machine. Instead, they have an official pipeline running on GitHub, and GitHub is running on some cloud, like most likely Azure.
And then they generate the package, they use certain authentication method to publish the new guide packages to the public feed.
And this entire thing is running in the cloud, like not running on personal account. They have a couple maintainers in their personal account just in case of emergency, like if they got stuck or they want to quickly unlist a thing, they don't have to go through the process and set up a pipeline. But I think that can be improved.
Then, the concern was mainly coming from Microsoft. Like, one day, a couple, like, Microsoft folks reached out to me saying, hey, like, we're shaping this product for very critical customers and insurance.
And they ask this valid question and we need some help from you because.
We, like, our product uses this open source component, and according to the policy, we're not supposed to take a binary artifact directly from the rest of the world and give to customers, so we have to take the source code and compile that purely inside Microsoft.
Like, because we have a lot of, like, antivirus, all these, like, scanners running. But the problem is, we also have a, extensibility story, so we have the ecosystem. We want third-party teams to be able to build plugins. So now we have this public OpenTelemetry, Microsoft internal OpenTelemetry, they share, like, the code is exactly the same.
We're debating, like, because we have two different packages, and for the plugins, they don't depend on this.
Which one are they going to depend on? You don't want to have two telemetry SDKs, right?
yeah, so then I have to work with the compiler team, also, like, C-sharp, like.NET inside Microsoft. So, we figured out a solution, and then we worked with Google on similar solutions for a couple other languages. What we did is, the C-sharp compiler has a flag which will enable the reproducible build. So, reproducible build idea is if you have the same source code, same command line argument input, and this, like, operating system has to be roughly the same, like, you cannot do two things on one on Linux, one on Windows, that will be different. But if you have a relatively similar environment, you have the same input, then for the same source code, you will generate exactly the same binary. The checksum would be 100% the same. The timestamp is just a checksum, not a real timestamp. Then, after that, you can timestamp it properly, whatever, but then you have a way to compare what you compiled versus what others compiled.
And if they're identical, then you know either either, like, both of you are good, or both of you got attacked, right? So what we end up doing is we still have the OpenTelemetry thing going through the public domain on GitHub, building and publish, and we… the only thing is we enforce reproducible build.
And then within Microsoft, we have 2 teams. One is the donut runtime team. The other one is my team, and we do this build independently.
And for… for both, those pipelines, we do a cross-check, so we check the three versions and making sure they're… they're identical. Then we know at least the public one is not hacked. And we ever, like… we haven't seen that, since the past two years, but… Our hope is if the public pipeline, if the GitHub machine, the VM, the infrastructure got attacked by someone.
or they have, like, binary injection or something, then within Microsoft, we would be able to see, oh, the output binary is not identical anymore. Then we can… first, we can investigate and see who got, like, affected.
Right? Number two is, if the open source one got attacked, we can contribute back by working with the community to fix the problem before it got, like, spread across the board. So… I know a couple of other languages, like Golan, maybe like Java, did a similar thing. So this is more, like, I see a great collaboration with, like, something you won't be able to do purely in open source, and with a corporate, like, open source collaboration, we have a solution here. So for the email one, I… I kind of feel it's probably the similar situation, like the corporate email can… Help you to get additional confidence, although there is no such enforcement.
Charlie Eriksen 00:29:49 Yep.
Yeah, that's totally fair.
Reiley 00:29:54 Yeah.
Charlie Eriksen 00:29:55 I.
Reiley 00:29:55 some of these stories like the like the I feel like when I talk to people, they're saying, this is great. And even, like, other product maintainers, because some of them use OpenTelemetry, so I talk to them, I try to learn, for example, from Kubernetes, how they handle security. And I also look at OpenTelemetry downstream.
Folks like how they use and and I have the luxury to.
talk to both the Microsoft, like, enterprise customers, and open source product will take on open technology. So, and this is why, like, during our email exchange, I also suggest, like, hey, if you're interested, I want to work with you to put some blog posts, because this security thing is not, like.
like, black and white thing. It's kind of like finding a reasonable path, like, carve out a path, and find the balance. Also, the balance could change. Like, today, we kind of, like, say, we trust people by default.
And I think that's based on the… Experience like we're, we're seeing very low chance of people like attacking the supply chain, but with AI, with all this, like, like all the fights among the countries, like balance might shift.
I wouldn't want to see at some point we distrust by default. That would be crazy for me, but I think that that balance.
Is being affected by many things right now and especially for.
For AI, like, I also work with some, like, startup companies in the UK. They run the fast testing for some OpenTelemetry projects, especially when we receive data.
And I can tell the number of security findings have increased dramatically because AI is doing awesome job.
So, yeah.
So I think there are three follow-up items. So first, based on your feedback, I picked a couple of things. I think that's very obvious. Already talked to the maintainers, and there's some alignment. I also got some feedback. So on one side, they're going to take some fix.
On the other side, I'll organize a meeting with you and the maintainers and the technical committee. I really want this communication. I think this is great to raise awareness. Then on the other side, I also think.
some of the topics are very interesting, and the balance is changing, and I… I do think, like, you have… you have better experience than me, based on, like, my gut feeling, like.
reading through your emails. So, I… I won't… to see if you're willing to like work with me and other folks to make some contribution there. Don't treat it as you're helping open telemetry product. I think this is more like you take open telemetry as an example. This is like an important open source software. But some of the struggles and the learnings and how we think about this problem and how we carve out a path like, how do we balance those problem. You can see there are a lot of principles. We don't want to be jerks. We don't want to discourage people who are not employed or some… like, we want to be neutral there. We want to welcome them. On the other side.
we also have this concern, are we going to be the next XCUTLs or something like that? And do we… like, although the maintainers might come and say, I take care of my email account seriously, I don't think how I'll be vulnerable, but we know this is… just, like, trying to lie to yourself, like, everyone, like, we're all human, like, we can make mistakes, right? So is there, like, an extra layer? So these are the great things I want us to… capturing some… some form of a, like, blog post, then on one side, people in OpenTelemetry will have more awareness, and also for the downstream, like, people who use OpenTelemetry, they also understand some of the challenges, and And I hope that can also encourage other, like, enterprise companies to say, hey, we see this gap, and maybe we can contribute something similar to, like, what Microsoft has done for OpenTelemetry.net.
And… and for you, I'm… I'm not sure, like, how it can help you. So, so far, it seems like you're trying to help us. You gave the feedback, and I'm trying to leverage your… your, like, strengths and the experience.
But if you, you think this would also help you, I want to understand a little bit, like, how I can better help you, because I, I'm, I'm running… the security shake, and I'm part of the technical committee. Is there something I can do to… Like, help you better.
Or keep you like more motivated in working with us.
Charlie Eriksen 00:34:33 I mean, so there's a couple of motivations here, right? One is that… I mean, the most personal one is that every single time there's a supply chain attack, it ruins my weekend.
Right? It's like a week worth of stress, because, like, every single attack is, like, super stressful.
So really trying to… the more we can reduce the attack surface, hopefully the… we can reduce the amount of attacks, and make life a little bit nice of everybody.
From a… More corporate perspective, right? I mean, OpenTelemetry is huge. I don't know what the stats is, but I am quite certain that we have a very significant amount of customers that use OpenTelemetry, right? If we can help protect that product, we're going to protect our customers.
With this specific research, I mean, I have contacted now about 100 different companies.
And the idea is that if we can kind of spread the awareness, eventually that word will travel, right? So people, you know, talk over, you know, beer, you know, on a Friday, you know, with their friends that work in different companies, they go, oh yeah, we just cleaned up our NPM, we found out that There was some stuff there, and then they go, oh, maybe we should look at that Right, so I've had some companies also be interested in, like, you know, co-publishing together and stuff like that, and one of the things that I learned from dealing, especially with the Shai-Hulud attacks.
Right, the interesting thing about the original Shai-Hulud attacks is that, at that time, the delay from us detecting the malicious packets until it was actually taken down Was, like, 8 plus hours.
And… We realized that in that time, the best thing we can do is to scream as loud as possible and work with our competitors also, because they have access to a set of companies and people that we do not have the ability to reach.
Right, so the more that we can all work together to spread the word, do not pull, you know, don't run npm install.
Whatever you do.
Reiley 00:36:45 Yep.
Charlie Eriksen 00:36:45 The more people we can protect.
So in this specific case, right, the more we can have people kind of talking and spreading this awareness.
Around, like, this is something you should look at.
the better. And I also think about it, like, do you remember back in the old days with, like, SSL apps?
When people were checking their SSL, like, what ciphers and stuff they were using?
Yeah. Right, they basically made it so that anybody could go and check, like, this… website, right? Is it securely configured?
One of the things I really am hoping is that we can also create a little bit of pressure within ourselves because there is no good way of checking right now. What's the status of this scope?
And maybe people will make informed decisions based on that.
So, that will also then create this, like, hey, we really want to adopt this thing, but for us to be able to do that, we need this and this, right? I think, you know, hopefully reasonable things. So, also, to have… give people the ability to measure themselves, like.
How are we doing? Because right now, it's just a kind of annoying thing to go and check. If we can make it easy, people will drift out of alignment with ideal. I mean, to even reach the ideal is difficult most of the time. The easier we can make it for people to detect and remediate when there is something out of whack.
You know, this initial push is going to be a little bit painful, especially in these kind of hybrid situations where the governance is open source, it has corporate side and non-corporate.
Yeah, that initial one is gonna be a little bit more tricky.
But hopefully, down the line, you know, I mean, everybody's used this from the ISO 27001 or SOC 2, right? It's just, like, NPM tends to be a little bit of a blind spot, but people know how to do this, right? Off-boarding and all these kind of things, regular audits and checks. So it's nothing new, it's just, like, we need to just spread the awareness a little bit. That's what I really want.
Reiley 00:38:47 Yep.
and like… to your point, I think that's also, like, why I would love to work with you on a blog post, because, like, raising awareness, even for some of the maintainers in OpenTelemetry, I think they're very good at the technical design, the feature work. When it comes to security.
I don't think, like, all of them have this, like, very good understanding about what problem are we facing. Some of them, like, might not even see this enterprise level Problems, and they should, because people are relying on them.
And… and for the… awareness part, I also have a related topic, so I can briefly explain here. So in the OpenTelemetry security SIG, We have a role that's the maintainer. Currently, it's only me. And… for the maintainers, they have the permission to see all the privately reported security vulnerabilities. So the idea is when people report security vulnerability, if they know this is a very specific thing to maybe, like, OpenTelemetry, like Java.
then we want them to directly go to OpenTelemetry Java maintainers. Like, that's the same as the Kubernetes, like, security-safe model. But, when… when people have this, like, cross, like.
across multiple projects, security concern under the OpenTelemetry umbrella is saying, I see this potential, like, if you send telemetry, I give you a response, I can embed something malicious there to just, like, cause DDoS attack, or maybe I can just cause a zip bomb or something.
then that thing might apply to multiple, like, telemetry SDKs, like OpenTelemetry Java, OpenTelemetry Node.js, and .NET. Then it'll be strange if they just publish one advisor under a particular product, or they just do this independently for all of them.
The goal here is we want to have a way that we can handle certain situation that requires a lot of coordination across groups. And then we also learn from the past that there are people who don't feel this is a particular technical problem or they don't even… have a GitHub account or something, so we don't want to draw a line by saying you must have a GitHub account in order to publish Security Advisor, because many of them might be customers.
that, like, they use software, but they're not essentially, like, software developer working on GitHub. So, this is why, and also, like, you know this, otherwise you wouldn't reach out to me via the email, so… For those emails, currently, only these two groups of people would see. Number one is the six security maintainers for OpenTelemetry. That's essentially myself right now. And then there are a couple product-level admins.
And those admins, they have been working with us for a long time, so we know them. And I think all of them are coming from a corporate background, so I've seen some of them in person. I've also seen them almost every other day on the video chat.
My question, or this is something I need advice, is I also try to grow the SICK security by trying to recruit other members. So far, I've only recruited two members, and one I already know in Microsoft is working in my team, but now he's leaving, and another member I haven't seen in person, but is passionate. So my… like, I constantly have this struggle with myself. If I need to grow this community, I want more people here to help.
How do I trust them?
Like, I don't… for example, like, how do I trust you? Like, what I did is I looked at your email, I did some search, and I saw you had some, like, public speech on YouTube, and based on those things, I think you're not coming to this space on day one, right? So I feel like I kind of have the trust. Then, based on our conversation, I think what you explained, it's reasonable you have deep knowledge there.
then maybe, like, at some point, like, if you're willing to, I'm also willing to, like, help you to become a part of the member. Like, this is a product for you to experiment something, and I feel like, so far.
Our engagement have the trust, but the question is.
am I doing the right thing, and can I… like, for example, if the XCU tells hiker or someone similar to that situation, they try to leverage that. Like, this is the weakness, right? So, they try to leverage that. Is there a way Like, what should I do there? Like, how do I tell they're, they're, they're coming from, like, a good intention?
So that, like, when I think about this, eventually put me in a situation like, hey, now I understand, like, why Microsoft would have a third-party company doing the security background check, because that's a hard thing. If I'm doing this, it's, like, almost like a full-time job, right? I won't be able to do it. So… here's… here's my struggle, like, I… I know that if I recruit someone running the OpenTelemetry 6 security, they would have the power to see a lot of security concerns before it's publicly known by the others. And they have some channel, they know some enterprise companies who want to subscribe to those things. But how do I trust these people? And how do I trust the subscribers?
I'll give you one example. If there's an XYZ company coming and say, Riley, we saw the information on the SICK Security homepage, and we want to be added there so we can know the unpublished security advisories at the first place, so we can work with our customers. How do I trust them?
I know if it's like Google or Meta, those big companies probably will trust them by default. But if there's a small company I've never heard about, and I know I don't have a full-time job to do the history or anything of that.
I'm you. You can see my struggle there.
Charlie Eriksen 00:45:02 Yep.
I think my initial reaction is that for me, trust is consistency over time.
Reiley 00:45:13 Yep.
Charlie Eriksen 00:45:15 Of course, it doesn't work in a case like, XE, right, the whole Geotan.
Reiley 00:45:19 Yeah, it's that consistency until it starts.
Charlie Eriksen 00:45:23 Yeah, that's the problem, right? Because the reality is that the information that you have has financial value.
Reiley 00:45:33 Yes.
Charlie Eriksen 00:45:34 So that's a really tough situation to be in, right? And that's one of the interesting… Tensions, right, about open source, right, is that we are, that we are building stuff that has financial value, right.
to a lot of people, right? You're commoditizing, like, you're making it a common good, but also, I mean, you look at, like, all the work that AlphaOmega is doing, right? The whole Linux and OpenSSF side of things, right? A lot of the… Big registries are saying this, right? We have a funding issue.
Right, because, like, we don't have the money to hire people, right, and… Especially the OpenSSF people have been saying this, right? The cost, like, the reason why doing something like an NPM, all of these kind of things, why it's so expensive, is not the bandwidth. It is the security.
Reiley 00:46:26 Yeah.
Charlie Eriksen 00:46:26 Umm.
Right, so as long as you're not funding it, right, if this is a problem.
Right, you're always going to have to do with these, like, I guess we'll have to… Yeah.
It's a really tricky problem.
Reiley 00:46:45 do you even see, like, some other… is your experience, like, as you probably work with other open source community, do you see some of them might have a different, like, way Or at least something that they try to explore. For example, I'm very curious about this. While talking to people in OpenTelemetry, I don't think anyone know if there's a case. Do you know if there's any open source community? They have third party.
Like, entity doing some audit to track the individual, like, background or something.
do you see anyone saying, if you want to make a contribution, you have to sign the CLA, and also you opt in for a security background check?
Charlie Eriksen 00:47:33 Mmm.
I mean, so I think this is two different things, right? One is being able to contribute and get up.
Right, and there, you always have the controls around, like, a trusted contributor needs to actually, like, sign off, right? One or more, kind of, reviews on it.
Reiley 00:47:49 If I can.
Charlie Eriksen 00:47:49 Powered.
Reiley 00:47:50 Yeah, the power of a merge or a publish or something that can affect the users. Yeah, so for the contribution without the power, I think that part I'm not worried too much. For the power part, I do think like a lot of CNCF projects, they have the funding.
like Cncf. Like they have the the membership like platinum, like gold tier or something. So they they do have the budget. And I said that because there are folks who run the the performance and scalability tasks, they have dedicated machines that we use, and OpenTelemetry actually pay for it, and the money is coming from the Cognitive Computation Foundation. So we mentioned this, like, funding. I think there are problems that can be solved Technically, there are problems that can be solved by money, and there are problems.
problems that probably can be solved by money, but not just purely by technical stuff. I'm trying to understand what you're thinking there. For example, wearing a Microsoft hat, is there something like maybe Microsoft can do for CNCF? I'm happy to explore the ideas.
Charlie Eriksen 00:48:59 Thank you.
Reiley 00:49:00 I'm exploring, and you have more observation than me. You have experience working with other community. So I want to learn what options do I have. I want to first go broad and not limit myself to, hey, we don't have funding. We cannot do this.
Charlie Eriksen 00:49:15 Yes.
Reiley 00:49:15 want to ask those questions, like, why? Why can't we? Maybe we can do this. Let me just explore it. And I'm happy to be proved, like, wrong in the end.
Charlie Eriksen 00:49:26 Yeah, I actually, I'm not sure what the good answer is here.
Yeah, I think, I mean, you can look a little bit at How… It's done in like other foundations, right? Like OpenJS Foundation, right? They have a bunch of people because they cover such a broad set of packages also.
Right? Where they have, like, more kind of cross-functional, right? They're all… Basically, they have more economics of scale, I guess, in some way.
And.
But they also have more interests, which… Makes it easier, right? Because like different companies can contribute different people, that kind of thing. And it basically becomes kind of the internal tension, right? Through the different interests kind of balance these all out.
So you're in it together.
I think that ends up working quite well.
Right once you have that scale.
Yeah, I, I don't know, it, it feels like maybe you're in a weird.
Size or stage of organizational foundation, like, kind of, the group?
like… Yeah, because there are just some things where like, I mean, like.
like, when it comes to security, right, this kind of idea of, like, four eyes for everything, right? Somebody else needs to approve other people, kind of, so nobody has the ability to do risky things completely on their own.
But that requires you… To now have a certain amount of people.
For that to ever work.
Right, yeah.
Reiley 00:51:04 So we started to have, yeah, so in OpenTelemetry, we started to have that. Previously, it's more like when people file security advisory or reach out to us.
it's like, hey, we have time, then take care of that. But there's no such, like, process or, like, clear expectation. So at least now we have established a rotation, so if people, like, create an advisory or they reach out to us through email.
Every week, we know someone needs to do that. There's a primary, like, quote-unquote, like, on-call.
Yeah. Except for you really have your cell phone like beeping. So they're the primary and secondary on call. And so far, I think we haven't missed anything. So at least we respond, like we give people first time response and we try to keep that in two business days.
But I… I also have the issue, like, two business days. Currently, it's very UI-centric, so if, like.
Because most contributors in OpenTelemetry are based in the US.
then the… the problem got tricky, like… like, I always ask myself, what if a problem happened during the weekends, or maybe during a U.S. public holiday? What… what do we do?
So it doesn't seem like having the business day purely based on EOS makes sense in open source products. I'm trying to improve from there. And also for individual sakes, like NPM, all the things like the OpenTelemetry, we're trying to encourage them to follow the same model that the OpenTelemetry Technical Committee has been following. But the difference is, in OpenTelemetry Technical Committee, we have like, we always have, like, about, like, 8 or 9 members, so doing this rotation kind of makes sense. Although I can see some… some folks there, they don't have a corporate motivation or something, it's just, like, they feel the obligation, they want to keep their… technical committee had, then they feel like they have to do the job. On the individual product SIG, the situation is the worst, because some of them only have, like, two maintainers. So there are, like, two people who have the power to publish a package. And If one is on vacation, another is having the public, like, holiday or something.
ask them to do this formal rotation, it's impossible.
Charlie Eriksen 00:53:26 Yep.
Yeah, and that's where at some point, like, especially once you have these, like, little, you know, groups of one or two people for individual… Things, right, eventually you have to.
consolidate up.
Reiley 00:53:42 Yeah, so currently, we're in the backup model. So, for example, if there's a SIG, they only have two maintainers, they couldn't cover it, then we're trying to cover it from the OpenTelemetry technical committee. And if people are not covering that, by default, it goes to me, as long as I'm working I'll try to handle that within a day or two, but there's no guarantee.
Charlie Eriksen 00:54:06 Yeah, I mean, it almost sounds like you need to have somebody.
Kind of a… vulnerability… Coordinator.
Roll, right, that basically sits across and is kind of the back line for everything.
Reiley 00:54:21 Yeah, currently that's me. Yeah. And I need to grow, the group, and… and then it goes back to my previous question, like, I… I have concern, like, how do I group? I mean, I can… Microsoft folks who I work with, then I… by default, I trust them.
But for people who have zero knowledge about their background, what should I do? So it's like a constant challenge for me. Oh, another thing I want to mention, something I learned recently.
In OpenTelemetry, we have people putting their GitHub alias and also the Slack channel. We talk to them, we know the account, but we don't have a formal registry. So I've seen the cases where maintainers added wrong folks.
Like accidentally. So I'll give you one example. People come to OpenTelemetry, a certain repository saying, hey, there's a security.
vulnerability. So they report that through the advisory, which is, like, only private, only, like, the maintainers and the security… security SIG, and the org and the meetings can see. So maybe, like, a handful of people there. Then… I was trying to add the maintainers. When I look at the maintainers, I saw from GitHub homepage, I saw you have, like, 3 folks there.
And then I tried to search Slack. I could only find one.
then I did that maintainer, saying, hey, like, seems to be yours, so I gave the link. And I'm not worried, because if… if I found a duplicated name, that's not the maintainer, they won't be able to open the link.
So I was sharing this. Then they start to add another maintainer. I just realized, oh, that maintainer decided to put the name on Slack as cat. So they don't want to use their own name. They just call cat or something like dog. So they joined and they start to have deep discussions.
They talk about technical things. I was like, where's the third maintainer? Can we add the third maintainer? They start to, like, dig through, and they couldn't find the slide. When they find some name that seems to be similar, they add it.
And the guy, John, I was saying, I have no idea, like, you probably added the wrong one.
And then we just realized, like, gosh, we shouldn't do that. So the first thing, like, I noticed is, do I trust Slack as a communication channel for those things? I don't.
Because people can add others without, like, any permission check or anything, it's hard to track, right? So I want Slack to be a way that people just, like, hey, like, they try to ping you, they try to say, hey, here's the link, you have to take a look, we have a security issue. Then if you don't have permission, you click the link.
You won't be able to see that, so I don't have the concern. Then the second thing we're trying to do, I already did that for the governance committee and technical committee, is to have people listing their Slack identity there. So you can check whether this is… You don't have three people all calling themselves Riley and you don't know which one is true.
So, yep.
Yeah, so… This is more like a.
the… I feel like, a social behavior. So, like, people People tend to… Like find your name and they trust you by the name, but I, I think name is something super unreliable.
Charlie Eriksen 00:57:49 Yep.
Reiley 00:57:50 And Slack, I also think, is an IAM tool. It's not designed to handle security advisory. It doesn't have audit logs, doesn't have any, like.
Like rigid history control, like you can delete something without others knowing.
Charlie Eriksen 00:58:06 Yep.
Yep, that's a big issue, right? The whole question of identity, how do you cross-link identities between different platforms and synchronize permissions and all these kind of things?
Reiley 00:58:18 When trying to push for extreme, I thought about this, like, hey, if I try to replicate the thing, like the technical committee and the governance committee have done, I start to ask the individual, like, repository maintainers to put their name on Slack, and also has a… like, acknowledgement, saying, like, they understand the obligation there, they're willing to join the rotation, and if they don't want to join the security rotation, then we'll remove them from the maintainer. Just, like, don't give them the power.
Charlie Eriksen 00:58:52 No.
Reiley 00:58:53 So this is something I'm thinking, but I can understand it might hurt people's feeling. Like, they might be very good at technical judgment, they just, like, work as individual contributors, saying, I don't care about security. So… So I try to put some careful wording there, saying maintainers should take care of the security. And most people agree. So we start to put some policy around this.
My, my fear is.
I don't have a corporate two to hold people accountable. This is more like a mutual contract. So someone would agree and they don't do that or maybe we'll take action by kicking them out. And so far we haven't done that at all.
Charlie Eriksen 00:59:38 No. Okay.
Yeah, I mean, that's the thing, right? At some point it becomes responsibility, right? When you're publishing meaningful and significant packages onto the ecosystem.
There is a contract in terms of, like, you're going to do your best.
2.
You know, be responsible for it.
And.
Yeah, it's a tricky question, like, for sure.
Reiley 01:00:02 Okay, so I noticed we're on time. So thank you for spending the time with me and thank you for.
Charlie Eriksen 01:00:08 No problem.
Reiley 01:00:08 listening and sharing your ideas. So, I'll… I'll follow up on the meeting between you, the technical committee members, and the Node.js project maintainers. Meanwhile, for the blog post, I can send you my Slack account, and we can chat on Slack if that works for you. I'm not sure, like, if you're using those tools.
Charlie Eriksen 01:00:31 Yes, absolutely, that works.
Reiley 01:00:33 Okay, then, okay, so expect an email from me, and we can continue on Slack. If possible, I hope we can maybe have this blog post targeting before the end of the month, if that works for you.
Charlie Eriksen 01:00:46 Sounds great.
Reiley 01:00:48 Okay.
So thank you so much, Charlie. Thank you. Have a good one.
Charlie Eriksen 01:00:52 Thanks. You too. Bye.
