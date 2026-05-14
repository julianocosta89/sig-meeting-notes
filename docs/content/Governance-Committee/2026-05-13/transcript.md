SIG: Governance Committee
Date: 2026-05-13
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:00:23 Hey, Tigran.
Tigran Najaryan 00:00:31 Hey guys.
Trask Stalnaker 00:00:33 Hey, Josh.
Hi, you're in Redmond!
jmacdonald 00:00:53 I… I am, hello. I'm having trouble finding the screen where I talk to you. Come on.
Yeah… There it is. Hi, Trask. I am in Redmond.
Trask Stalnaker 00:01:06 Yay.
jmacdonald 00:01:07 Yeah.
Trask Stalnaker 00:01:08 Nice.
jmacdonald 00:01:10 I've met my team.
Trask Stalnaker 00:01:14 Your first time there?
jmacdonald 00:01:15 Yeah.
Yeah, here all week.
Juraci Paixão Kröhling 00:01:23 Hello, hello.
Trask Stalnaker 00:01:26 A…
Ted Young 00:01:28 Hello, hello!
jmacdonald 00:01:31 Hello?
Hey, Ted, I got one for you.
Ted Young 00:01:35 Yeah Oh, shit! Wow.
Trask Stalnaker 00:01:39 that from…
jmacdonald 00:01:41 Really early days at LightStep.
Ted Young 00:01:43 Yeah.
Juraci Paixão Kröhling 00:01:44 That's 2017, 2018, like.
Ted Young 00:01:47 Yeah.
jmacdonald 00:01:47 Oh, I like that.
Juraci Paixão Kröhling 00:01:49 Yeah, I remember tracing is fun from our open tracing workshop here in Berlin, KubeCon Berlin.
Do you remember that, Dad?
Ted Young 00:01:59 I do, yeah. Those were the early days.
Juraci Paixão Kröhling 00:02:02 Dude.
Ted Young 00:02:02 Therefore.
Juraci Paixão Kröhling 00:02:03 Yeah, they had an open tracing donut shop demo, wasn't it?
Ted Young 00:02:07 Yeah.
That was back when Priyanka was still working at LightStep.
Juraci Paixão Kröhling 00:02:12 Exactly, yeah, she was at DevRel, I think.
Ted Young 00:02:15 Yeah, she was… she was in charge of marketing, so it was, like, me and Priyanka pitching tracing, and then she went on to run the CNCF for years.
Juraci Paixão Kröhling 00:02:25 Yeah, I remember that we went there with USB sticks with the container images, or whatever images, for the Go dependencies, because, you know, the Wi-Fi wasn't reliable.
Ted Young 00:02:37 Yeah.
Very briefly, Josh, just because you're wearing that shirt, I don't know if you remember, Casey Chen from… light step days, but she was the engineer there. We used to have these, like, see-everything, like, hats that our designer Duncan had made.
jmacdonald 00:02:58 She was like.
Ted Young 00:02:58 I lost my hat! God, does anyone have one of these? It was my favorite hat. And then, like, the next week, I was cleaning my basement and found one, not even in a box, but, like, sitting under a pile of boxes.
So, that was my funny old Lightstep swag.
jmacdonald 00:03:16 Nice.
Ted Young 00:03:18 Anyways, we probably have real things to talk about, and I have to leave after the first 30 minutes, unfortunately, just FYI.
Dope.
Let's see… Oops.
Tigran Najaryan 00:03:46 From the agenda, Doc, there's no real things to talk about.
Ted Young 00:03:51 Nothing.
Tigran Najaryan 00:03:52 Yeah.
Ted Young 00:03:53 Nothing important going on.
Josh Suereth 00:03:56 I'm debating what to write, but…
Alolita Sharma 00:03:58 I think Josh has a whole stack.
Jack Berg 00:04:02 topic I could talk about.
Josh Suereth 00:04:03 Excellent.
Jack Berg 00:04:03 debating as well. It's like, when there's an empty agenda, it just… your mind starts going.
jmacdonald 00:04:11 Riley asked me to…
Josh Suereth 00:04:12 meetings.
jmacdonald 00:04:12 say something as well, but I have a feeling that Josh's topic is going to bring it up, so I will stay silent.
Josh Suereth 00:04:20 No, no, no, please, please add your topic. I'm still for… like, I did not have enough coffee this morning, and I was flooded with meetings, so I'm way behind, and my brain is still in 12 places, so I didn't have a chance to think ahead of this meeting, apologies.
And I'm doing all this vulnerability stuff, so I'm still, like, that's in my head. Anyway, so please add your topics, it'll take me about 5 minutes to actually solidify my thoughts.
Ted Young 00:04:52 Yeah.
I just have an FYI, you know, so… Small thing happened, you know, we graduated. Woo!
In case somebody missed the news there. But, that's fantastic. But we are still on the hook for… for finishing… You know, what we were calling stable by default, but it's really, like, how do we, like, put a bow on all the things we promised people originally and get it shipped?
The thing is, the OTEP as it stood was because it was based on some horse trading between us and the CNCF about, like, what is the scope of work? The end result was, like, you know, written in kind of, like, vague, highfalutin terms, and so we need to sort of… take that current doc and rewrite it into, like, a set of, like, actually actionable roadmap items that we can turn into work streams. Because it was a little open-ended, the way it was, like, currently… currently written. So I've been gathering those requirements, I've been presenting them at the… the Spec SIG, And I'll have a 2.0, you know, doc with hopefully better work streams next week for y'all to take a look at.
And I think part of doing that work, we don't have to take a lot of meeting time to talk about it right now, but I think part of doing that work is, like, I think also a place for us to then figure out, how do we do better roadmapping? You know, how do we, involve the maintainers and the community more, in these efforts? And I think we've been having success as, like, the first step of that by just talking a lot more about the different work work streams that we have in the specsig. So, that's been actually feeling really positive.
And I want to figure out a way to kind of scale that up so that it's not, you have to come to this meeting, or you have to know about the meeting recording and want to watch it to get this information.
So, would love, you know, we can ideate on Slack about how to do this, but yeah, I would love people's ideas for, like, how we can… Kind of do that better, and get more maintainers and other people involved.
So that's… that's my bit. You can watch the SpecSIG recording if you want to know the current state of that thing.
Pablo Baeyens 00:07:41 Will this mean a new OTEP, or… How are we going to?
Ted Young 00:07:47 Yeah, so we currently have an OTEP, so I guess my plan is to rewrite that with a new OTEP, but because it's, like, 5 work streams, you know, I don't know if, like, one OTEP you know, the question is then, like, how do… fine, let's say we hit approve on that OTEP, like, what's next, right? Like, how do we… how do we then, like, run those work streams in a way that is public and has, like, community involvement? And I know, Pablo, you've been doing work on, like, how do we, like, visualize these things? Jack, you were doing some work there, So I think that's part of it, but yeah, that's something I would like to work with everybody once we've, like.
Gotten some agreement on those.
scope of work? Like, how do we actually, like, accomplish those things?
a little bit better, and with more maintainer and community interaction. Like, there's a good chunk of these things that are owned by a single SIG, or it's like a single SIG is, like, delivering the tools to the rest of the community to do some work and stuff like that, but I think one giant OTEP is not enough.
to get cooking, really, right? We'll have to take a step after that.
Josh Suereth 00:09:02 I didn't raise my hand, but just to jump into that, Ted, I would… I think, finding someone who feels responsible for each of the pieces you've outlined is going to be important. So just, you know, it could be more than one, but there needs to at least be one who is like, I feel responsible for this, I'm going to drive it forward. And I think that's what that OTEP needed all along, was just, here's the three work streams, here's people who will own it, and want to… Right. Yeah.
Ted Young 00:09:28 Yeah, and it's just, like, the… also, some of them were just so vague, right? Like, we needed… for anyone to even want to own it, like, I was trying to go around and get people to own these things, and they're like, what does it mean, though, to take this on? Like, I don't want to take on an open mandate, like, what am I taking on? You know, so… so that's what we'll have next week, hopefully.
I saw a hand raised.
Trask Stalnaker 00:09:51 It was me. I was, yeah, the… we never got good buy-in from maintainers on the current OTEP, like, I was just double-checking, there's zero maintainer approvals on that OTEP, just only GCTC.
So, I think that's gotta be part of… Whatever we do next.
Ted Young 00:10:15 Yes.
100%.
And maybe, if we can't get good buy-in on one, my next step will be to just break it into an OTEP for each work stream, you know, because maybe that's part of the problem too, because it's just too much in one spot.
But I hope just making it actionable and concrete would be enough for people to be like, I see who's trying to own what, and what my responsibility as an SDK maintainer would be in this workstream, and to have thoughts about it.
I think this also relates to, you know, we… through the, Felt it, once again, you know, trying to get, like, system packaging off the ground, which is, like, an important part of… Shipping, you know, Not… not, like, a new project, so much as, like, here's how… a way to, like.
finish shipping the stuff that we already have, and that was, like, once again, you know, something that we're trying to run this process that we've created for ourselves, and it felt, I think, like everyone involved was, like, just kind of frustrating, and it felt kind of painful, and… So, I think… for the rest of these work streams, it's a good opportunity for us to figure out, like, what's just a better governance model for this project that gets the maintainers more involved and feeling like they have more agency, you know, gets more work off the TC's plate so it doesn't feel like a full-time list of chores to be on the TC? You know, how do we get, you know, like, spec sponsors or other stuff?
So I think figuring out how to do this work that's, like, not the fun work, in the sense of it's not, like, cool, next-gen, like, oh, we're working on some, like, computer science problem that's interesting, or something like that. Like, but nevertheless, stuff like maintainers, end users, lots of people care about.
This is just a good opportunity for us to, like, iteratively improve Improve our model there.
to hopefully get to something that feels like it's more public, more people are engaged, you know, it doesn't feel so crazy-making to be on the TC, that kind of thing.
Okay.
That's all I got. Pablo, I think you got the next one.
Security?
Pablo Baeyens 00:12:44 Just… just a quick one. I moved the, document that we've been discussing for some time now, to the Sikh security repository, I guess… the TC should approve it, and… I think also the SIG… a lot of the SIG security approvers are here, so… I guess, or a couple of them, so I guess please, those of you who are sick security groups, I especially… I'm interested in the room.
Trask Stalnaker 00:13:19 Do we think it's worth adding… updating the security MD file?
Either for the whole org, or for the collector specifically. Like, trying to think of how this helps to… for maintainers, to guide them on how to address advisories that come in.
But if we want to… Possibly short-circuit some of those.
the SecurityMD file is… It's probably the… The best chance we have of somebody reading that before they submit a vulnerability.
Pablo Baeyens 00:13:59 I'd be happy to do open PRs for that, but I would want to get this one approved as before. I got the suggestion to adding it here on the security response page as well. I can do that, but just let's… let's agree on the wording on Seek security, and then I can put it everywhere else.
Ted Young 00:14:23 Jack, you wanna lead a maintainer incentive discussion?
Jack Berg 00:14:27 Yeah, I'd love to. So, I've been floating this idea in a couple of contexts. I've been talking to Ted about it internally, I've been talking In various forms with the TC about it. And, you know, we have this call once a month, and so I thought it would be good to bring it up with you all here.
I think we need to provide more incentives to be maintainers. I've kind of been typing along during this with some of the ideas here, but basically, you know, maintainers are the lifeblood of the project. They do all this necessary and unsexy, unglamorous work that keeps the machine going. The issue triage, the PR reviews, which are increasingly laborious and cumbersome in the AI era, with, you know, with it being the bar to make one of these PRs so low.
Running releases, security advisories.
and more, and we put an immense amount of trust in our maintainers. They have the publishing keys, they hold the keys to the castle, and, you know, every one of them is like an attack vector to a supply chain attack. And so, like, you know.
Anecdotally, I look around at SIGs, including the ones I'm involved in, and I think many of them are staffed very thin at the maintainer position. There's, like, just a few people that are, like, holding up, you know, a large foundation, or, you know, a large amount of weight. They're very load-bearing. And so, yeah, like, I want to come up with incentives to help solve that problem, to encourage people and companies to want to target being a maintainer, to want to do this unglamorous work that is so necessary to the project's health.
And, you know, another part of this is that being a TC… being a maintainer is… is really time… time intensive. You know, we talk about things in the TC about, like, our security SLAs and our security posture, and we want to, like, we want to have guarantees for security patches in this amount of time. Like, how can you ask people to do this if they're doing it in their spare time? Like, I think, practically speaking.
If we want this to be a project that executes at a high standard, we have to recognize that being a maintainer in that type of environment is a professional activity that, while not exclusive to people that are doing a 9-to-5, is… is… is… is indexed in that direction. Like, it's hard to be a maintainer if your company is not sponsoring you, or is not approving some sort of time commitment that that entails. So what do we do about all this? Like, I want to see more people want to become a maintainer, and I want to see more companies want their employees, want their staff to pursue maintainership. How do we create the incentives that drive that?
You know, like, that's what it's all about. Like, incentives produce results. And so, I'm looking at the… I just sketched out some ideas for some incentives to, you know, give some elevated permissions, privileges, like, things to… to maintainers, so that it's not just burden, right? Like, becoming a maintainer doesn't just mean you're loaded with a bunch of burden on your shoulders, you also get something in exchange for that. And your company that's sponsoring you get something in exchange for that. So, I see some hands up.
I'll open it up to discussion.
Juraci Paixão Kröhling 00:17:56 Jack, you're not leaving us hanging here, are you? I mean, you said you had some proposals. I'd love to hear that before I… before I give any opinions.
Jack Berg 00:18:04 Okay, yeah, they're written down here. So these, these are just things that are just, like, they're off the top of my head. I'm not committed to any of these, but, like, you know, I think we need to create, like, a grab bag of, like, you know, rewards, incentives for maintainers, and that's just, like, one thing. And so, you know, we have this roadmap mapping activity. We did this OTEL Unplugged conference, you know, earlier this year, and, like, we did this exercise where everybody threw out a bunch of topics, and then people voted for the ones that they think are important. And, you know, there's this bubble-up thing where, like, the most important one's at the top, and, you know, it's… OpenTelemetry is a federation of people. It's not a hierarchy. We can't force anybody to do things, but it's meaningful when the organization structure goes out and publishes what our priorities are going to be, what we want to invest in more, what we want to invest in less. So if maintainers have a say in that, if maintainers have, like, this exclusive exclusive privilege to be able to vote on our public, you know.
our public document that says what we're investing more, what we're investing less in, that is a reward. That's an idea. So, you know, maybe some sort of exercise that we run on once a year, twice a year, something like that, where we talk about what we're prioritizing and maintainers get to participate.
Project proposals and acceptance.
You know, the TC and GC, we… we deliberate, and we, like, you know, we fuss over which projects we accept and reject, and the maintainers, you know, we're under-leveraging their opinions here. Often the project proposals that we are accepting or rejecting, mostly accepting, I'll say, like, end up being very impactful to maintainers who have to, like, take that, like, commitment to more work, and it gets trickled down to them, into their priorities. They should have a say in the things that we are going to accept as projects. They have a lot of, you know, knowledge about the current context of their respective projects that should be incorporated into our project acceptance criteria. So that's another thing. How can they vote? How can we create, like, some sort of gate on project proposals that requires you to go out and get consensus among maintainers before your project is accepted.
Another idea, restrict who can propose projects. Like, you know, you have to work your way up the organization ladder. You have to work, like, prove that you're committed to this project before you can propose a project that is so impactful to everybody.
You know, say that only maintainers can propose projects. That's another gate, and it's another reward structure.
Another idea, this one is maybe… I don't know if people will like this or not, but, like, voting for the GC. Should everybody have the same say?
I don't know, maybe, or maybe the people that are load-bearing for the project should have an elevated say. Maybe it's like a two-to-one voting type of thing, like, you know, voting classes in a corporation, something like that.
And then those… that's the extent of my ideas. I think the other bullets were added by other peoples. Now there's 5 hands up, I'm going to officially cede the floor.
Juraci Paixão Kröhling 00:21:13 Nice, thank you very much, Jack. I think that this is… So interesting. I… timing matches what I heard from or Sean, earlier this week, or last week.
where, Sean was asking… so Sean Marciniak, I think he's at Splunk now.
he was at Atlassian before, and one thing that he pinged me, and I think he pinged Pablo as well, perhaps, is that be an opening from the project to provide feedback to maintainers or contributors?
to funnel that back to their managers, so that they can talk to their managers and say, look, I'm doing great work here at the community, and it is valued, and can I get a promotion? Like, a way that, people can get feedback, like.
Community feedback or internal feedback, and then have it in a semi-official way, and have benefits within their organization for that.
I like this proposal. This is a proposal 3420, or the issue 3420 on the community repo, so the link is here.
And I think it goes in the same direction, or in a similar direction. So I'd like to see, like, people being recognized for their work on… as a maintainer, or as a contributor, and having benefits on their day jobs for that. So I think this could be one way, or one benefit.
my former manager at Grafana, so she had a very good view on, like, the incentives of open source contributions.
Like, the three things are, the project needs to want to receive the contribution, the company needs to have a financial incentive in giving you time, like paying your salary to work on that, and the maintainer needs to have a personal interest in doing that. Like, if I don't like OpenTelemetry, I'm not going to work on OpenTelemetry.
And typically, you only see good contributions, or sustained contributions, from when those three stars align, right? So, when the project wants, when the company pays, and then the person is working there on their Because they like it.
I like your points there, but I think there is one part that is missing, which is the company incentive. Like, what are companies gaining from those contributions?
I don't know. One thing that we did discuss last week during the GC call was the situation of a specific vendor Well, not a specific vendor. I mean, this is not specific to them. We just walk… through the boots at a sponsor showcase at KubeCon, and you see OpenTelemetry logos everywhere.
Right, so you see, we support OpenTelemetry, we are hotel native, we are hotel contributors, and so on.
And I think… I forgot who… who suggested that, but I think the idea would be, how about we create a badge of honor, or something like that, for companies that, can show that they have, that they pay contributors, they pay maintainers to work on the project, so they could show a badge on their, like, an official badge from the project, from the GC, or whatever, from the CMCF.
where they can show, like, it's for marketing purposes, right? So that's what companies care. Like, they… they… they pay people here because they… they… marketing-wise, they can go to their customers and say, we are hotel native, we are… we are… we are hotel. We are the creators of Hotel, right?
I mean, people do that. And I think we… it should… we should have a way for making that official, like, saying, this company is indeed a good citizen of hotel. I think those two would be good incentives for the companies. I agree with your points. I think they are… They are the benefits, but they are not incentives, I think.
And I think the incentives can be, can be more personal, like, more career-driven for individuals, and more… Marketing, or even, perhaps, for organizations.
Jack Berg 00:25:20 Yeah, I'll just say, like, a couple times I think I heard you say, like, contributor slash maintainer, and I think core to my proposal is that, like, not all contributions are equal. I know we say that all the time, but I think we want to disproportionately incentivize maintainership.
Because that really is the lifeblood of the project, and that is what is struggling.
Severin Neumann 00:25:47 I mean, my point was mostly what Jorasi said at the end about, like, I think the most important part is, like, if we support the companies behind the maintainers, it's much easier for maintainers to be sustainable, right? Jack, if I understand you correctly, this is about sustainability. And I think we all feel it the moment we work for a company that says, like, yeah, I pay you 10, 20, 50, 100% of your time contributing to open telemetry slash other open source.
projects, it's much, much easier, right? And I have been at a variety of positions where it was allowed more or less, to do those kinds of things. And I think, yeah, if we figure out those kinds of incentives where people can say, like, ISA, yeah, my company is really cool with me contributing, because, like, I and them get certain benefits out of that, or if we figure out a way how we can make it more, like, making you more hireable as being an hotel maintainer, where you're still like, hey, there's… whatever, a badge that we can give people that they can put on their profile, or maybe something where they can say, like, hey, I'm an official maintainer, or something like that. I think that that would help a lot, right? I mean, we have 100-something maintainers right now, so maybe there's also something where we have to figure out, like.
who's real, like, I like the thing that we have now that, like, maintainers become removed after a certain time where they're no longer contributing, because I think it should also be… like… a really, like, hard thing to… to stay and maintain, and to continue contributing. So I think those three things that… that are actually in conversation right now are highly connected, so yeah, I… I'm really, really eager to… to make this happen.
Ted Young 00:27:36 And… Just to jump on that, because I have to jet off to another call, unfortunately, but a thing to think about, something I've noticed is there's a mismatch between… like, where our labor force comes from versus the traditional OSS model of, like.
basically, like, time spent in seniority. Like, the idea is, like, you stick around for a long time, and you move your way up the ranks from triager to approver to maintainer, and, it's sort of like a long-term investment before you become an approver or maintainer.
But the way, like, things work at the companies that are paying people to work on this is, like, Joe Bob is maintaining X, Joe Bob is moving on in their career to something else, that company still has a team of people that's focused on this kind of instrumentation stuff, they would put someone else onto that project.
Or they would bring someone else in their team, they would rotate, you know, who's working on what. But that way that companies allocate people and choose to pay people is sort of out of alignment with that traditional, you gotta put in like, several years of effort before we're gonna trust you. So, somehow moving to a different trust model. It's not that, like.
you know, we… I don't think I want to have, like, vendor seats, because that feels frickin' weird, but… but there's a mismatch between how the trust model works, where it's like, companies like, we trust this person to work on this.
And, like, we're willing to pay them to work on it, but, like, how does that then line up with that person getting… getting fast-tracked in some way?
Morgan McLean 00:29:22 I do want to avoid anything where, like, companies can start parachuting people in. Like, Ted, you remember that.
Ted Young 00:29:26 Yeah.
Morgan McLean 00:29:26 conversations with, like, was it Mark when he was at Amazon, like, 4 or 5 years ago?
Alolita Sharma 00:29:30 Oh, yeah, yeah, yeah, absolutely.
Morgan McLean 00:29:33 Like, when I was happy with the outcome of that, I want to avoid a situation where the outcome would be.
Ted Young 00:29:38 Exactly, like, we don't… we don't want it becoming too pay-to-play, because that has other failure modes, but I'm just noting that, like, when we've tried to get more senior people in, people who would be a maintainer, they get frustrated by being, like, kind of gatekeeped at the beginning. So there's some… somehow, and it could be just that it's, like, easier to become an approver, you know? Like, becoming a maintainer's really hard, but maybe… like, like, like, approver tryouts are easier to get. Something… if someone is coming in through a trust network of some kind.
I don't have an answer to this, I'm just noting that this is part of… been part of the practical problems of, like.
changing the guard on, like, who's maintaining what, is it's kind of like this long process that's a mismatch with how companies would allocate resources if you had a conversation with them about bringing more people in.
Anyways, I have to go, but, I'll watch the recording for the rest of it. Have fun, y'all.
Jack Berg 00:30:42 Pablo?
Pablo Baeyens 00:30:43 Yeah, so just very quickly, the CNCM provides some benefits to maintainers, but we are not giving those to open security maintainers, because only the TC and GC are listed on the official maintainers list, and I think, like.
Probably those benefits are not enough, but, like, we should… Probably add more people to that list, so that they also get those benefits, and they have the individual incentive to.
Alolita Sharma 00:31:10 I think, Pablo, that's changed, because the CNCF has actually cleaned up that list.
I think it's more in line with all the We can double check, but I think they have been working towards that. It's not the GC and the TC anymore, I think it's also the SIG.
Oh, no.
Pablo Baeyens 00:31:29 I'm pretty sure it is the TC and the GT only, if you want to look at it.
Alolita Sharma 00:31:33 It's only that.
Pablo Baeyens 00:31:35 Yes.
Alolita Sharma 00:31:36 Yeah, we should definitely… I agree with you.
Jack Berg 00:31:38 So, to my knowledge… The privile… the privileges are, you know, the… the benefits are things like, I think that, like, Copilot, for example, has a program where maintainers of CNCF are, you know, have some enterprise access to Copilot. That's, like, an example, and so you have to be an official CNCF maintainer to get that, and, you know, the OpenTelemetry maintainers that are not on the TC and GC don't qualify. Do you have other examples?
Pablo Baeyens 00:32:06 I think ability to run to the Technical Oversight Committee is… probably, at least to both, it is gated by that. And then…
Alolita Sharma 00:32:15 Yeah, my…
Pablo Baeyens 00:32:16 participation in certain tracks in KubeCon is also.
Oh my god.
Alolita Sharma 00:32:20 Yeah, like, the maintenance one.
Pablo Baeyens 00:32:21 You gain sponsorship by somebody that is on that list, but, like, it would be easier if you were listed there. I don't think they are, like, huge incentives, but… solving that problem.
Severin Neumann 00:32:33 with us being graduated, but, like, yeah, I think especially, like, Maintainer Summit and Maintainer Track were… are blocked.
But I think that that thing aligns with, like, I mean, we have, like, if we figure out, like, who's the maintainer and, like.
Maybe we say, like, you only show up on this list if you have been a maintainer for a certain period of time. It's much easier to maybe fill up this list, because, like, adding 144 people there is maybe not the thing that we should be doing, but if we say, like, hey, people that have been An active maintainer for the last 12 months will be listed there, if we can maybe figure out a way, something like that.
I think that… that… that would… would already help.
Jack Berg 00:33:15 There's also practical problems with this, which is, like, what is the actual definition of a maintainer? I know we have a maintainer in the community repository that describes the responsibilities, but we don't list anywhere, like, or have a team that is, like, the superset of all maintainers. And so, Pablo, I think this actually relates to the work that, you know, that I was working on, and you picked up, you've been carrying on the torch to, like, model how we work with, like, workstreams.yaml. If there can be, like, a field for every SIG, That, like, captures the team that is the maintainers, then that can be the source of truth for, like, the set of teams that are considered maintainers across the entire organization.
And then when you have that list somewhere, you can do automation around it.
Right now, we just operate on convention, right? Where there's teams that end in dash maintainers.
But, like, it's not all the maintainers. Like, what about the leads of, like, the, like, the user experience, and, like, the Prometheus interoperability, you know, folks? Those are… those are maintainers by my definition. They lead these SIGs, but they're not, like, you know, their teams don't follow that convention, so, you know, by some definition, they're not maintainers.
Severin Neumann 00:34:37 But they should, right? I mean, at least for the end user's sake, they have a maintainer's group, and I'm not sure if Prometheus, but…
Jack Berg 00:34:47 Yeah, my point's just a minor one, like, let's formalize it, let's, like…
Alolita Sharma 00:34:50 Yeah, yeah, let's formalize it. I agree.
Jack Berg 00:34:52 Exactly.
Alolita Sharma 00:34:53 Agreed.
Pablo Baeyens 00:34:54 Yeah, I think there would be no opposition to formalizing that within Opendet, and then we can use that to have a conversation about adding it to the CNCM one, yeah.
Alolita Sharma 00:35:08 So I think, Jack, the larger question here is that how do we break this up into, you know, actionable, parts that we can take on and actually… formalize.
So that it becomes a reality, you know, sooner than later.
Jack Berg 00:35:26 Yeah. So, in my head, we have… we have these documents where we describe the different roles in the community. And, you know, there's, like, member, approver, maintainer. And, you know, we could elaborate on the maintainer section.
To have, you know, a subsection that starts to talk about some of the… some of the things that you get in exchange for being a maintainer, instead of just the things that you are responsible for.
And, you know, we won't be able to deliver all these things at once, you know, like, some of these ideas are just ideas right now, and they would take little projects or, you know, work streams or whatever it is to, you know, to turn them into reality, and so… Maybe the list starts small with something that we can act on right away, and we just… we plan on trying to grow it over time. And, like, each one of these ideas, each one of these incentives sort of is, like, independently vetted, independently acted on, and, you know, when it becomes a real thing, is added to that list.
Alolita Sharma 00:36:29 Yeah, I totally agree, because it should be an… it will be an evolution. It won't be just everything in one shot.
I mean, maybe having a, Proposal for incentives, which is, Then presented or discussed on the community repo.
Is a… is a good start.
Jack Berg 00:36:52 I'm hearing a lot of people nodding along to this general idea, and you know, I guess I sense enough support here that I can do a follow-up in the community repo, and I'm not exactly… I'll definitely start with an issue, but, like, maybe, like, a parent issue, and then start to carve out some sub-issues, something like that, and see where that goes. But, you know, I guess what I'm trying to say is I can take an action item to start to follow up on this and turn this into a real thing.
I can't do all of it, because I think a lot of this is within the GC's realm, but, you know, I'd love to collaborate.
Alolita Sharma 00:37:26 Yeah, and the thing is, Jack, we can definitely take some parts of it and then all individually also work.
With you on taking each part and kind of adding.
And taking that process across, because since we also work with the different SIGs.
you know, as we see sponsors, we can also, you know, have those discussions, and get that feedback from maintainers, to provide active feedback into the, you know, official issue.
Morgan McLean 00:38:02 I, so I strongly agree with this, and I have a big concern about maintainer burnout, and we need to have enough rewards for maintainers. Where I struggle is what those rewards would be.
Alolita Sharma 00:38:11 Yes.
Morgan McLean 00:38:12 that we discussed here, Jack, I think the first one you brought up seemed pretty compelling, but the other ones are all nice, but it wasn't clear to me if those will really move the needle for people that much.
like, that's where, in the past, when we've talked about this, I've really sort of hit a wall, is like, this is great, but, like, what can we actually do, like, practically… Rewards them for their work in a, like, a really tangible way.
Jack Berg 00:38:34 Yeah, so, let's put our heads together and maybe, you know, workshop this in the issue, right? Like, you know, I'm sure other people, when they sleep on it, will come up with other ideas. Yeah, exactly.
If we're all just aligned with just like, hey, this is an issue, let's try to solve this, then, you know, I'm excited to see what we can come up with collectively.
Alolita Sharma 00:38:58 Absolutely.
Jack Berg 00:39:02 Jurassi?
Juraci Paixão Kröhling 00:39:05 Jack, thank you very much for, you know, for leading this and for bringing this topic. I think it is very important. I think… based on the reactions that we're seeing here, I think it is… everybody agrees that this is… this is necessary.
I… it… Perhaps an unrelated comment here is that, People just need more visibility internally about what they do.
If that's the case, and not specifically to you, of course, Jack, but anyone here, and let your… the people in your CX know as well, that if you need visibility in the community, if you need to be talking about the things that you do.
In… out in the wide, like, just talk to the community managers, talk to hotel comms, or ping me directly, and we can… we can give you exposure. Like, we can give you… do, like, streams on Hotel Channel, YouTube, LinkedIn, and so on and so forth.
Sometimes all it takes is just a small exposure sometime, you know, talking about the thing that you do.
If that's what… what you need.
Talk to me and the community managers, we can make it work.
I know it's not the point here, but just saying that, you know, if you're here and if you need something, count on us.
Jack Berg 00:40:20 For anybody watching out there, right, too, because these are recorded, so…
Juraci Paixão Kröhling 00:40:25 Right, yeah. I mean, I don't know if anybody watches that, but, yes.
But, so… I think the message is spread the word here to all the people in your SIGs.
Gc people talk to your, to the SIGs you are the liaison for.
like, make it known that it is a possibility. Like, we have space for people that need some exposure.
Jack Berg 00:40:59 Alright, that topic has run its course. Lyudmila, you wanna take us… Yeah.
Alolita Sharma 00:41:05 Hello.
What's the good news?
Ludmila Molkova 00:41:09 Well, good news, bad news. So, I've left Grafana, I'm in between jobs, my next company is going to be Google, which means we will have 3 TC members… to Google.
It means one of us would need to resign. I was happy to resign, but I… I would… Let Josh speak about it, because he has other thoughts, which is a bad news for all of us.
Josh Suereth 00:41:38 It's not bad news. So, I'm, I, yeah, I'm planning to resign as a TC member. So, I think, First of all, Thank you for staying on, Ludmilla, and I think David and Ludmilla are great new TC members. I think they're doing awesome work. I think they're super active, and we can all agree, like, well-deserved on the TC. And, you know, I don't plan to spend less time on OpenTelemetry.
So I'm gonna make that crystal clear for everybody. But I do plan to step, down from the TC. I think we've done a lot of work in the TC, I think we're on a path to kind of change how OpenTelemetry works, and I think we're in this, like, changing of the guard, right? Where OpenTelemetry's been around for 6-7 years, and so active leadership is going to change.
I will still drive projects, I will still do things in OpenTelemetry, I will still maintain the things I'm maintaining. That's not changing. The amount of time I have from my employer to commit to OpenTelemetry has not changed.
But I do plan to take a step down, so…
Tigran Najaryan 00:42:40 I have to add you to the spec sponsors immediately, Josh, I think.
Alolita Sharma 00:42:44 I know.
Josh Suereth 00:42:47 Sure.
I also am one of the GitHub admins, by the way, so that is independent of the TC, so I still will continue to participate there. I might even have more time to do that, in the future, hopefully, so that Trask doesn't bear most of the burden.
Yeah, the other thing, I forget who I was talking to. Someone said, if you… if we wanted to change things, we could propose expanding the TC to 12, so that we don't have this limit of 2.
I don't care, personally. I will do the same amount of work for OpenTelemetry, regardless of if I'm on the TC or not. So, just… just to let y'all know.
Tigran Najaryan 00:43:29 We also need to, I guess, see which things you are listed as a sponsor on, and… whether we then mark them as being delegated, or maybe we assign a different person, that's something we can do in the TC, I guess.
Ludmila Molkova 00:43:46 We can do this next week, I'm still, almost 2 weeks away from the change, so we have a couple of more weeks of Josh being in the TC.
Morgan McLean 00:43:57 Gosh, your contributions to this project have been immeasurable and numerous, and… in the last few years, some of the absolute deepest for any individual contributor in the project, so…
Alolita Sharma 00:44:07 You'll be people.
Morgan McLean 00:44:08 missed, if you're gonna be missed, because, like, you talked about the expansion of the TC.
We talked about that at the last GC meeting. I think the GC is in favor.
Alolita Sharma 00:44:17 Yeah.
Morgan McLean 00:44:18 Regardless of, like, Josh, if it were to expand, I don't know if that changes your… influences your decision.
You're muted, Poke.
Tigran Najaryan 00:44:26 He's… he's… he's not… he's not… he said he's not going away, Morgan.
Morgan McLean 00:44:30 I know, but still…
Alolita Sharma 00:44:31 Exactly.
Tigran Najaryan 00:44:32 I can do exactly the same.
Morgan McLean 00:44:36 Essentially. But, so perhaps then, as an aside, we had discussed that just on the GC, because there was a desire also to get people more experience on, like, the collector and profiling in certain parts of OpenTelemetry, getting them more TC representation.
But I don't know if that influences your decision, I just wanted to put it out there before we… before this comes, like, a one-way path.
Josh Suereth 00:44:56 No, honestly, the only… this is gonna… I don't know if this… again, I want to talk with the TC about this a bit, but the only thing I'm really concerned about losing is proto-maintainership for the protocol.
Because actually, I don't think we have a lot of people on there, and it's been kind of, like, just a few of us that really, like, evaluate those changes and kind of push through. I did a bunch of triage on that repo before, and there's a lot of just low-hanging fruit to fix.
literally the first thing I plan to do is every meeting this hour, I'm going to be spending on the Proto repo for the first couple weeks to try to get ahead of things there. Regardless of if I'm a maintainer, but if I'm not a maintainer, it's gonna be harder to, like, make changes there. I just, like… anyway, that… we talked in the TC Recharter around having, like.
Maybe pulling apart Some of the maintainerships of these things into a set of core individuals.
We talked about having Emiratus. I would love to see that make progress, but I'm happy to just, like, let you guys do that, and then I can, I'll just react to whatever happens, right? Like, I will still be here, I'll still be active, I'll still be making changes. That's the key thing I want you all to know.
Severin Neumann 00:46:07 I mean, if it turns out that you're not staying at the TC because we not expanded, I think another reason why… why shining more lights on the maintainer is important. I mean, it's not only you, but many other maintainers that do, like.
amazing work, and are not in the TC, are not in the GC, and I think we really need to figure that part out to, yeah, elevate them. Because right now, it's TC, GC, And then we need to figure out, like, having, like, senior maintainers, principal maintainers, whatever, to say, like, look, there's amazing people doing amazing work, right?
Ludmila Molkova 00:46:53 Okay, I'll finish. My first thought when I heard it was, no, no way, Josh is the most influential person.
Alolita Sharma 00:46:59 Really not that tough.
Ludmila Molkova 00:47:00 cannot happen.
Alolita Sharma 00:47:02 We'll… we know where to find him, so…
Ludmila Molkova 00:47:11 Okay.
Let's move on.
Oh, Josh, it's yours.
Josh Suereth 00:47:18 Yeah, well, this is… This is basically a follow-on from that, because I thought this might be important. So basically, like, what do we want to do around TC sponsorship next steps and follow-up? I do think, like, like Tiggin was saying, we're going to have, we're gonna need to have a discussion about the things that was leading and what happens to them. I do think, We had a bunch of discussions in the TC, and I think in the GC about the packaging sync, and about sponsorship of that. And I do want to get to a point where we can make sponsorship decisions on these project proposals relatively quickly.
And I also want to get to the point where we have more visibility onto what's going on and kind of expectations there. So, you know, we kicked this off, man.
What's the year now?
I think it was November of last year, maybe even November of the year before, was when we started doing some of these TC revitalization, charter stuff.
and… to some extent, I think a… what do you call it in Scrum? A retrospective is due, right? What's working? What's not working? What do we like? What do we keep? What do we change?
I think it's absolutely worth doing that. And so I… we have 10 minutes.
we could do a retro, like, in the next month. I won't be here, but we could do… you could do one in the next month, or we could do a quick retro now, where folks can off-the-cuff just say, hey, what do we think is working, what do we think is not working?
I'd like to kind of follow up with that offline and do some, you know, changes, based on that in the next, like, 3 weeks while I'm still going to remain on the TC.
Morgan McLean 00:49:07 I strongly agree with the desire for retro, I think it's… it'd be very, very valuable, especially at this juncture.
Josh Suereth 00:49:18 Go ahead, John.
Jack Berg 00:49:21 Are we gonna… are we gonna kick it off now, or are we gonna wait a month?
Josh Suereth 00:49:25 I was gonna say, if there's anything, like, that's obvious to people that they want to say, like, let's start now. Like, I think we have 10 minutes, unless folks have something else they want to use the 10 minutes for, just getting some of the ideas out of things that we felt went well, or poorly, would be good to kind of hash out a bit now.
Jack Berg 00:49:43 There's just… there's just this tension that is… that comes up, and I think we need to address it somehow, which is we want to address these proposals quickly.
And, and we want to gate them, or at least we have historically wanted to gate them on TC sponsorship. And, and TC sponsorship is… is scarce. Elevated TC sponsorship is a scarce resource, and, And also, elevating TC sponsorship is, like, a big-time commitment. Like, when I committed to declarative Config, it was, like, 15 hours a week for 3 years.
So, like, that, like, you have to shift your life around for. So, how do we… how do we… how do we, how do we make sense of that? Just, like, that we want to resolve these questions quickly, but these questions are impactful.
Josh Suereth 00:50:37 Yeah, to respond to that briefly, I want to say that, TC Sponsorship is, I think, akin to leading a project, and 15… hours a week for a year or a couple years is, I think, on par with anything significant happening across OpenTelemetry.
So, like, when we think of this, like, config work.
we're basically asking the person who runs it, hey, are you willing to commit about 15 hours a week for 3 years? Because that's… that's the size of project in OpenTelemetry.
And if anyone disagrees, let's go talk about when we tried to go 1.0.
And our ability to estimate that, right? Like, these are significant things. So I think that's a really good call-out, Jack.
Anyone else?
Morgan McLean 00:51:38 Also, to shoot from the hip, like, in terms of things we've done, like, just generally the evidence of, like, the project's success, OpenTelemetry's everywhere, we've achieved all our original goals, that is fantastic. Like, as someone who's here from the beginning, we have grown and landed in way more places than I ever could have imagined.
For areas where we've struggled, like, I look at spots where I've been involved, like… profiling still hasn't completely landed, and I'm involved in that one, right? Like, like… but, like, it still hasn't landed. I had hoped that would come in faster.
That one's been particularly interesting, because our usual failure mode in OpenTelemetry for projects like that are not enough people get engaged, it sort of withers on the vine. Profiling has huge engagement, right? There's a lot of people working on it.
And so that one's a bit of a unique failure mode, where it's just complex, the ways it interacts with the rest of the project are complicated, we don't have a huge amount of profiling expertise on the TC, though I don't think that's been the major issue for it.
But it's worth looking more into that, to, like, how could we do this even more effectively in the future? The typical failure mode of a lot of these are things withering on the vine, that's more from maintainers or contributors disappearing, and it's usually on tangential things that aren't as critical, so, like, it's regrettable that some things like network performance monitoring haven't done as well, but it's not… It's not a black mark on the project, like, that's fine, it's… we'll live through it, and the reasons for it are understandable. So those ones worry me less. I don't have a whole lot of existential concerns, but, like, there are definitely things we could improve.
Like the profiling case I mentioned earlier.
Josh Suereth 00:53:09 Pablo?
Pablo Baeyens 00:53:12 So… We set out to do some things… From… improving the workflow on previous GCTC meetings.
My feeling, although I haven't checked closely, is that we haven't followed up on most of those, or… They haven't been done… And at the very least, they are not being actively tracked, and that worries me. Like, I feel like… we, and I included GC here, are relatively bad at, like, this… Project management, like, task management thing, and… That makes it hard to improve both here and, frankly, anywhere else, because we don't have a place where we track things, and… Don't commit to it.
Josh Suereth 00:54:08 That's… that's a good point. I think Jurassi's next?
Severin Neumann 00:54:16 You're muted.
Alolita Sharma 00:54:18 Dressy.
You're muted.
Juraci Paixão Kröhling 00:54:20 Of course, I'm muted, I'm sorry.
I have a similar comment to Pablo, like, I think we… And I can… I can go back to different contexts, like, we are… We're not the best example in following up on what we discussed.
In general, like, I can think about several OGC leadership calls, and summits, and on-person meetings that we had.
The items that we agreed to do, they were never executed on.
I think this is something that we… and I'm using the GC example here, because again, this is… On me as well.
So I think we… we ought to be better at, following up and, actually doing the things that we're promising to do. I can also think about Hotel Unplugged, like, there were… I love the event, I love the energy, but my feeling is we had quite a lot of people discussing about things that they are not the ones implementing, they are not the ones doing things.
And then, like, quite a few things were not being followed up on. I'm very happy that a couple of them were.
Most of them, as far as I know, from what I'm standing, they are not. They… they were not… they were just discussed there.
So I think this is one. And the other thing that I think we could be… We could do a better job, perhaps, is… On a main… on a… on a… the role of maintainers, I think we could have a clearer message that maintainers are not only the people who merge pull requests.
They are people who… Are responsible for their communities.
Like, they're small, that is not small. They're, the individual pieces of the project.
Yeah.
So, I think that's all that I'm gonna say.
Jack Berg 00:56:18 Just a quick response to that. So, like, I think we struggle to follow up with these things, because the follow-ups, like, it's easy to say, hey, I'll go follow up with this, but practically, like, the follow-ups are tough. They're, like, big consensus-gathering activities in themselves. One of the follow-ups from this, from the, the MCP server,
Alolita Sharma 00:56:40 proposals.
Jack Berg 00:56:41 like, action items was that I was gonna go and, like, model what things… what projects TC members are actually sponsoring, so we can actually have, like, reporting on this and know where our effort is being spent. That's still ongoing, with Pablo picking up the torch and that, and, like, you know, we're… it just… things move slowly. Partially because of everybody has commitments elsewhere, but partially because, like.
It's just necessarily slow.
Juraci Paixão Kröhling 00:57:08 So, I think that's a good example of how it should be done, and I'm totally okay with that. What I'm mostly concerned about is Having discussions and not having people in the discussion that is actually gonna take the action item to actually work on it.
Right, so making decisions for other people to work on is very easy, and it's nice to have a discussion and then just brainstorm, or bike shed, I think, is the term that I heard the other day.
I don't think those are productive, like, we should not… We should probably have a… I don't like red tape, I'm not for processes, but I think… Before really engaging or starting a discussion about what we should be doing, we should determine, like, who are the people who are actually interested in doing the work.
So we don't spend time just talking about things.
Josh Suereth 00:58:00 Okay, we have 2 minutes left, so 1 minute each for Alolita and then Josh. Sound good?
Alolita Sharma 00:58:05 Yeah, yeah. Thanks, Josh. Again, needless to say, you know.
whether you're officially on the TC or not, you're, you know, a core part of the project, so thank you. And, you know, again, we have lots to do together.
So, but I did want to go back to the comment that Jack made, that, hey, you know, it's just so hard to gather consensus when we move forward on any follow-up, and I think that, Jack, to that point, it might be easier to not have individual ownership so much, but also, like, tag team, you know, pair up.
like a GC and TC member, you know, it's worth the effort to kind of have a multiplier effect, brainstorm, move ahead, what do we do, you know, kind of an, divide and conquer kind of an approach, because it is hard to, you know, for an individual to kind of go and get A large community to go and provide buy-in.
And at the same time, I'd also like to say that the… I think the GC sponsor model has worked quite well, in terms of bringing in, you know, maintainers a bit closer to being able to reach out to the GC, and I think that the, if the TC liaisons and GC sponsors actually Team up a bit more closely, you know, then I think that that can actually have a multiplier effect on some of the work streams that we've, you know, wanted to do, but Lost momentum along the way, or, you know, just gotten too busy with… multiple other things. But I'd just like to call that out, that let's team up, because, you know, it's just that everybody doesn't have to do everything individually. We are a… we are all a part of the same team.
Back to you, Josh.
jmacdonald 01:00:10 I don't think there's time for me to say what I was going to say. I will put a remark into the shared Slack. I think it's better that way.
Given that we're out of time.
Thank you.
Josh Suereth 01:00:22 Cool. Thanks, everybody. I'll follow up on Slack as well. Like, that was a great discussion. Hey, guess what I'm gonna say, based on also what we're talking about? Let's find action items and owners. Yes. So, we'll do that in Slack.
Alolita Sharma 01:00:34 Okay, sounds good.
Jack Berg 01:00:37 I made a project board.
Alolita Sharma 01:00:39 Exactly.
Josh Suereth 01:00:40 Oopsie.
Alolita Sharma 01:00:41 Thanks, Jake. Bye.
Armin (Dynatrace) 01:00:44 Bye.
