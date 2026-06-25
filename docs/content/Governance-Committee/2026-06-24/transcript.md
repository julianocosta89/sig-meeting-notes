SIG: Governance Committee
Date: 2026-06-24
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:22 Hello.
**Marylia Gutierrez** 00:26 Hello!
**Pablo Baeyens** 00:28 How's it going?
**Marylia Gutierrez** 00:30 You?
**Pablo Baeyens** 00:32 I'm fine, I'm… Survive me of the heat, I guess.
**Marylia Gutierrez** 00:39 How bad is it, Ria?
**Pablo Baeyens** 00:42 36, 37 Celsius?
**Austin Parker** 00:46 Oof.
**Marylia Gutierrez** 00:49 Toasty!
**Austin Parker** 00:53 That's rough.
**Severin Neumann** 02:09 Hello!
**Marylia Gutierrez** 02:11 Hello.
**Alolita Sharma** 02:43 Hey everyone, good morning.
**Austin Parker** 02:46 A.
**Severin Neumann** 02:58 We have quorum, right, with 6 people, so Tad Santi is not coming, Morgan said he's not coming.
**Marylia Gutierrez** 03:04 Yeah.
**Severin Neumann** 03:05 Who's missing your RCSync?
**Marylia Gutierrez** 03:07 Yeah, that's true.
**Severin Neumann** 03:08 Yeah.
Do we want to get started, then?
**Marylia Gutierrez** 03:18 Yep.
**Alolita Sharma** 03:19 Yes.
**Severin Neumann** 03:21 I think I had added a few topics One of them is, like, a private topic, so maybe I… we… we can do that one at the end.
The first one is probably not even taking 5 minutes.
So the Dodge thing… And Flutter's thing is moving really good.
I'm not sure if anybody looked at the proposal. Also, the DART team from Google came back and they said, like, hey, we are not building something ourselves right now.
But we're super excited about this thing happening.
So, Sarah.
On board on… on… on this happening.
And one thing I wanted to get out before, like, say, we make any more progress on it is the Call for Contributors blog post.
So Michael, The person who proposed all of that.
Created that, there's the pull request, so… I'm fine with it, but maybe what some of you could just… Glance over it if it's… good to go, and then I would ship it Maybe tomorrow.
So that we can get a little bit more attention on it.
And then maybe next week, or the week after, we can… we can talk about Going forward with it. Yeah.
Thoughts, comments?
**Marylia Gutierrez** 04:43 Yeah, I can take a look at the blog post as well, yeah.
**Alolita Sharma** 04:46 Sarin, is there a link? Sorry.
**Severin Neumann** 04:50 It's in the… it's in the, meeting notes. It's the… pull request to the I.O. repo.
But I can also put it in the… in the.
**Alolita Sharma** 05:01 Oh, this one, okay, okay. No, no, found it.
**Severin Neumann** 05:04 Okay.
**Alolita Sharma** 05:05 Yes, thank you, thank you.
**Severin Neumann** 05:07 Yeah.
**Alolita Sharma** 05:08 I was just looking at the industrial proposal, I think that's pretty cool.
**Severin Neumann** 05:14 Yeah, that's… that's… that's the next topic.
**Alolita Sharma** 05:18 Okie do.
**Severin Neumann** 05:18 I want to add something to the… To the… to the DART one.
I thought I'd put this also on the agenda, because I also think it's an… it's an interesting one, because it's a new kind of thing, because, like, I don't really think, like, this is something we have already.
So, so, so it feels like the idea is to build something around more like a… kind of vertical, like everybody using OpenTelemetry in more an industrial use case. There's a few people that are interested in that.
But now the big question is, like, what are we doing with that one, yeah?
**Alolita Sharma** 05:55 Agreed, agreed. In fact, you know, in Japan, I'll be presenting on some of the work that we are proposing from Apple for industrial in telemetry. So that's, again, a very, very cool intersection. I have a talk in Japan on that with the… with our, some of our teams that are actually working on IoT.
**Severin Neumann** 06:26 So just to add that, what they mean by that, like, they mean, like, manufacturing, IoT.
**Alolita Sharma** 06:31 Gotcha.
**Severin Neumann** 06:32 Devices, legacy system, industrial protocols.
**Austin Parker** 06:36 It's got a…
**Severin Neumann** 06:36 There's the… Yeah, there's things about Modbus, MQTT, and a few other things. I think Josh shared something about, like, a water system.
He is…
**Austin Parker** 06:49 Oh, yes, because Josh is a part-time water baron now.
**Alolita Sharma** 06:54 Yeah, yeah, that's true. Yeah. But, we are presenting on MQTT and manufacturing, so that's…
**Austin Parker** 07:01 Yeah, I mean, MQTT is not just manufacturing, right?
**Alolita Sharma** 07:05 Yeah, that's true. But it is a very common…
**Austin Parker** 07:09 Yeah…
**Alolita Sharma** 07:10 Standard.
**Austin Parker** 07:11 Yeah, yeah, yeah.
**Severin Neumann** 07:17 So my…
**Austin Parker** 07:19 Posting about them.
**Severin Neumann** 07:21 So my thing is, like, I find this also, like, super exciting. I also know Lukash, who is, like, he and I work together at Cisco a lot, and I also have chatted back and forth with him on that. So I think this is, like, on the one hand, like, a super cool thing and an idea, but at the same time, it's very different to most SIGs that we have today, right? It's not, like, something that easily fits like, if… like, it covers so many things at the same time, right? It's not like that they say, like, hey, we want to do open telemetry for IoT. Like, it's this multidimensional thing, so… maybe that's a good thing, I don't know, but it feels like, A very broad scope.
So yeah, I just wanted to see what we think about that, how we… can make them move forward. Is this even something like… or is this something that should live in the end user SIG, or any other SIC, or… yeah, I don't know.
**Alolita Sharma** 08:20 No, it has its… I mean, it has its own discipline and intricacies. So, just like the mainframe SIG, when we started it, you know, it was coming in with a very specific footprint, hardware footprint and environment. Similarly, this also has that, you know, there are several industrial standards, and, if that can be, you know, kind of Integrated, because there is a lot of stovepipe telemetry implementation in the manufacturing segments, you know, for different types of manufacturing.
And, but there are lots of standards also that the industry has built over time, so MQTT UA and other, standards are something that can easily interoperate with, hotel, with OTLP.
So that's… that's kind of… it can become very interesting, depending on who is… but you need the users, because I think that folks who are actually in that business will make this successful. It cannot be folks who are, you know, just thinking about it and find it as a hobby.
**Austin Parker** 09:30 Yeah, I mean, I think, ultimately, it's just… there's gonna be as… It's immature, there's gonna be things that have a… Just a different shape, you know, much longer tail of…
**Alolita Sharma** 09:44 Yep.
**Austin Parker** 09:46 Both.
Work output, but also adoption.
**Alolita Sharma** 09:52 Yeah.
**Austin Parker** 09:53 I don't really know if there's a… Bad.
Side 2 minutes!
**Alolita Sharma** 10:05 I think the only risk, as Severin said, is it's a very broad area, so to kind of scope it to a.
**Austin Parker** 10:12 Specific.
**Alolita Sharma** 10:13 areas which we can make progress in, right? Because you can have.
**Austin Parker** 10:16 Yeah…
**Alolita Sharma** 10:17 discussions, but… To kind of have a goalpost.
**Austin Parker** 10:22 Yeah.
**Severin Neumann** 10:24 Yeah, give… giving… I think it's, again, like, this whole discussion that we have, like, every time we add a SIG, like, we add overhead.
To our community, and we talked a lot about, like, where do we draw the line with our scope.
So on the one hand, I'm also… slide.
intrigued by this topic, and like, hey, let's do this, but at the same time, I know, like, hey.
It also comes with the same overhead as everything else, like having a… Lia saw, having a TC sponsor, having, like, all this logic… logistics around it.
And, and so I'm… I was wondering if we… if we could… Give them space without, like, turning on the full machine.
And see, like, how far they gap before, like.
Before, like, putting all of this into a SIG, so… yeah.
**Alolita Sharma** 11:23 Yeah, so… I mean…
**Austin Parker** 11:25 I guess my point is, though, is, like, I think it's… decent.
my understanding, at least, of, like, the industrial space, and, like, also things like… like FinOps, right? Like, we keep constantly… trying to get better alignment with, like, sort of the FinUPS people around CENCOV, and… They just work differently.
**Alolita Sharma** 11:49 Yeah.
**Austin Parker** 11:51 Like, it's the… the pace is different, right? Like, it's not… because the people… because the stakeholders are different, I guess is the best way to describe it, right? Like, I think the same thing is probably going to be true in industrial, just thinking, like.
Just as, like, a random, you know, Example of this, I remember… Before, way back in the day.
my academia years, I was working on research for traffic signaling, and just… you know, like, traffic lights… are programmed in Ada, I think?
You know, like…
**Alolita Sharma** 12:31 Still.
**Austin Parker** 12:32 Yeah, like, and, like, the big, the big thing now is, like, oh my god, you can write Luis scripts.
is insane.
The pace of both discovery and adoption of things is much slower.
in these fields, I think. And so… it might be okay to say, hey, this is sort of the meeting or the SIG for this, and we don't really expect anything to come out of this for a while.
But we want… We want there to be a place… we want to be able… we want to be able to say, hey, you're interested in this, here's where you go and talk about it.
And I think having that kind of… having a sort of, like.
Like, literally, it's a SIG, right? It literally is a special interest group.
**Alolita Sharma** 13:22 Yeah.
I know.
**Severin Neumann** 13:29 definition, yeah, but again, like, I mean, that's why I think I find it very interesting, because, like.
if we want to scale out those things, like, I mean, today it's industrial, the next time it's maybe another topic, the question is, like.
How can we capture those kinds of groups?
And give them space in our ecosystem and community.
and not every time, like, go through this whole project proposal management, and, like, saying, like, hey, and now you have a liaison, and a sponsor, and here's all the logistics around it, versus, like, hey.
just use the OpenTelemetry community to meet and have your things going on, right? And I don't know, it feels like something… That… that's a good example for that.
To… to rethink that a little bit.
**Alolita Sharma** 14:19 Yeah, I agree.
So, and, and again, as I shared, we are definitely going to, from Apple, introduce Some specific areas that we want to see, in that.
Space, so this is very timely.
**Severin Neumann** 14:44 Rask, I think you're… we cannot hear you.
**Alolita Sharma** 14:48 Were you saying something, Trask?
**Trask Stalnaker** 14:50 How about now? Yeah, there we go. Yes.
**Alolita Sharma** 14:52 I can hear you.
**Trask Stalnaker** 14:53 The only thing I'd add is that we also want these groups to be successful.
**Alolita Sharma** 14:59 Yes.
**Trask Stalnaker** 15:00 In the community, and that's sort of what this… these… You know, we have spun up groups before without following these things.
And they have… been… often unsuccessful.
And… died out. So that's sort of… the only other side that I would… Want to call out.
**Alolita Sharma** 15:33 Actually, Tresk, I'll follow up with, Lucas and talk to him, because I worked with him on the end-user SIG, for the Blueprints project, so, I'll chat with him and see, you know, where he won… he is… what is he specifically thinking about, because to Severin's point, it's such a vast area. And then, you know, we are very specifically interested in some of these supply chain, telemetry, standardization, you know, intersection with OTLP, and, you know, there's a lot of work actually happening in the industry, so we want to kind of see If, that can be a specific use case, then we can help drive that.
So, I'll chat with him, and then maybe Severin and I can come back to it.
Next week.
**Trask Stalnaker** 16:23 And Severin, is there more… I mean, like, they have the issue, right, and that's good for gathering… folks who are interested. They can put out, you know, a blog post, sort of, to gather interest.
to have a… sounds like they already have a Slack channel, to discuss things and, you know, build interest.
Is there, like, is that enough?
For them at this stage, until they, you know, come back with Staff, you know, like, staffing and goals.
Or is there something else that you were wanting to give them as, like, SIG-ish?
**Severin Neumann** 17:08 I… I think the question is, like, maybe… So what you said, like, they now have a Slack channel, they are building out this community. It's really a thing I like, right? They are very enthusiastic, they're building something out, and maybe this could also be a kind of a blueprint for… let's not call it a SIG, but, like, a community of interest in the open telemetry space.
let's say that's moving towards becoming a 6. So maybe we can write something down where we say, like, hey.
Not everything has to be a SIG from day one, and, like, even outside of the OpenTelemetry official or community, you can do things, and here's, like, the things you can do. Open a Slack channel, hotel, dash, whatever you're doing.
create a repository, here's how you should license it. Like, maybe we…
**Trask Stalnaker** 18:02 Not a repository.
**Severin Neumann** 18:04 No, no, the old, like, like.
**Trask Stalnaker** 18:06 Oh, yeah, yeah, yeah.
**Severin Neumann** 18:07 work, like, have your own hotel… hotel-whatever, GitHub org, but we give you some guidance on, like, hey, if this ever comes something official, maybe there's some things you should have an eye on, so maybe to build out a little bit more this ecosystem thing, right? It's just an idea, I'm not sure if this is a good idea.
**Austin Parker** 18:26 I don't want us to… I really don't necessarily want us to, like.
I get where you're coming from, Trask, around, like, are we setting people up for success?
I also just… I think we just… we need to be, like, I think, like, sometimes we need to go ask them, what does success look like to you? Right? Like, we should probably, like, respectfully, I don't… you know, we can sit here and talk ourselves in circles around, like, what-ifs and should's and whatever, like, all day, but I really think a… if there is interest and energy from people, then I think our best option would be just to simply go and say, like, hey, what are you trying to… like, what are you looking to accomplish? Are you looking to accomplish That, you know, hey, we don't actually need to… we're not trying to change anything, we're just trying to, like.
put a place for people who are working on this to come together and, like, compare notes. Okay, cool, right? Then maybe that's something that you can do as part of, like.
end user can help organize meetings for you, or whatever. It's a community calendar. You know, are you… are there, like, specific SDKs that are missing, right? Are there semantic conventions that are missing? Like, right? Like, I think… I think the thing that I see… Is that we are… We are so locked into this idea of, like, oh, there is such a high level of, like, coordination overhead, or…
**Trask Stalnaker** 20:05 Well, if I can get back to…
**Austin Parker** 20:07 to be… like, we want these things to have a… an outcome. They're very outcome-oriented.
**Trask Stalnaker** 20:14 100% agree with, and if I can go back to what you have started with, which was, if we see a body of motivated people, and they have a success criteria that is, you know, what does success mean to them?
Isn't that exactly what our project proposals are? That's all I look for on a project proposal.
**Austin Parker** 20:35 But I think that.
**Trask Stalnaker** 20:36 Because I look for…
**Austin Parker** 20:37 Question…
**Trask Stalnaker** 20:38 Do they have staffing? Like, it's not… I want to see that it's not just two people, you know, that are interested in this.
**Austin Parker** 20:46 But…
**Trask Stalnaker** 20:46 And I want to see what their definition of success is.
**Austin Parker** 20:50 Like, I don't think… I don't think we have a… a shape of thing that is just… My definition of success is getting people together who are interested in this.
Right? Like, we're very outcome-oriented, like, our entire thing is very outcome-oriented, and I think that is… not what this should… like, I think what's missing is, like, if… and again…
**Trask Stalnaker** 21:14 So you're describing a meetup. You're describing a meetup.
**Austin Parker** 21:17 I'm just.
**Alolita Sharma** 21:17 Really?
**Austin Parker** 21:18 I'm describing a special interest group.
**Alolita Sharma** 21:20 Yes.
**Austin Parker** 21:21 I'm describing a SIG, right? I'm describing, hey, we are people working in this area with this thing, and our goal is to… Have a meeting, have a place for people who are also working in this thing to come together.
And, like, talk about it and coordinate.
Not everything has… my point is not everything has to be, like, oh, we're coming together because we need SCADA or IoT… Semconf, or we need Hotel Lua, right? Like… maybe part of the… maybe this SIG, through meeting and talking about it, says, oh, actually, we do need Hotel Lua, and… Then that turns into a project proposal, right?
**Alolita Sharma** 22:09 Yes, yes, agreed, agreed.
**Severin Neumann** 22:11 I think we… at least what you say is very much aligned to what I was thinking about. I think the only problem is, like, sick as a word is already, like, meaning a lot of things in our community, right? It's something officially blast.
group of people that work towards an outcome, like a C++, like a mainframe implementation, and whatever. So the only thing I wanted to put out there is, let's say, give it a different name, like a Community of interest, or whatever.
And not, like, build another process around it. Just give them best practices, and just encourage them to say, like, hey, having your hotel industrial channel, this is exactly what we want you to do.
And by the way, we also want you to… or if you ever plan to have meetings, that's also cool. We can set up meetings or meet up, right? So really just encourage that behavior without, like, making it a whole process thing, right? To say, like, here's a document, if you have… are a group of people that want to talk about the same thing, do those three steps, and then go for it, and if you have a project proposal, come back to us.
Yeah, a light white sig, meet up, community, whatever we want to call that.
And this lives outside, like, like, they need their own GitHub org, they need their own, like, like, they're not blessed, so to speak, right? I think that's the difference.
**Marylia Gutierrez** 23:38 Yeah, because I was also thinking, like, if we just give the name sick, that also comes with the thing, like, we're expecting to have maintainers, approvers, things that we… they can continue, but we cannot say to the community, like, oh, yeah, you can expect to, like, continue, like, moving forward, except for this, that… that it starts creating, like, exceptions, starts to get, like, weird. So if it is gonna work differently, it should be, I guess.
**Alolita Sharma** 24:03 I mean, this… yeah, yeah, I agree.
**Austin Parker** 24:06 Again, like, I think… what's… I think… My recommendation is just, one.
let's just go talk to these people. Let's talk to people more and ask them what is it that you want to get out of this, and if it is just a meeting, cool, then we'll help them set up a meeting.
But also, I do think that we probably need… Especially as we get bigger, and, like, we will need to… We will need to find a way to plug people into this, right? Like, I think one of the things that… I think, kind of, winds up dinging us is that because we have such a high bar of… Like, we have a pretty high barrier to entry for people that just want to come in and meet up, right?
**Alolita Sharma** 24:55 Yep.
**Severin Neumann** 25:00 Yeah, and that's… I think we all agree on that. I think all we need to…
**Trask Stalnaker** 25:03 I like.
**Severin Neumann** 25:04 permission, and so I do that, right? This is cool, we are happy with you doing that.
**Trask Stalnaker** 25:09 And Jeff says, too.
**Austin Parker** 25:11 I think, I think, like, actually, I think the user group thing that Alita posted was a good idea, too. Like… Or community of practice, I don't know.
**Alolita Sharma** 25:20 User groups have been used in the open source world forever.
**Austin Parker** 25:27 Yeah, I mean, UGG. Oh, UGG.
**Alolita Sharma** 25:32 Hopefully it's not ug.
**Austin Parker** 25:35 That would be very funny.
**Alolita Sharma** 25:36 Right now.
Then we'll have a mascot, but, you know, it's good to have user groups.
I think that's the idea that the, you know, the CNCF has been discussing, the TOC has been discussing with the TAB to have, you know, community groups, and they call it, you know, labeled as technical community group, but any… whatever the name is, but that, you know, that… function exists, right? And it can easily be, as Marillia said, not a formal SIG with all the expectations that, you know, Dell places on SIGs.
But maybe a precursor to that.
If the, you know, if the community actually forms, then, and has good initiatives, then it can graduate from there, make proposals, then become, you know, formal sign on a specific deliverable.
On mission.
**Trask Stalnaker** 26:34 Yeah, we've had a few that I think would have benefited from this.
Whatever we're gonna call it, meetup user group.
Most recently, the networking SIG, the networking SIG that, you know, the… like, it is a… common, like.
Sometimes people need a couple months just to organize themselves and decide what they want to work on.
**Alolita Sharma** 27:01 Absolutely.
**Trask Stalnaker** 27:02 And so… and then we would get better SIG proposals out of that.
**Alolita Sharma** 27:09 Yeah.
**Severin Neumann** 27:13 Okay, so what I hear is like… oh, sorry, go ahead, Pablo.
**Pablo Baeyens** 27:18 And I was just going to mention another example, which is we have a channel for Open Synergy Collector on WebAssembly. It's not an official SIG or anything like that, but it has proven useful for people having conversations.
**Severin Neumann** 27:31 I guess people are doing that already. I think it's just helping people to say, like, yes, we want you to do that, right?
So, maybe what I hear is… what I hear is, like, two tasks now, so go back to that issue and what you said, Austin, like, ask them, like, okay, what do you need? What do you want? Like, do you want to form a SIG? Or would you… and then the other thing, maybe really put out a contributor guide that says, like, hey.
We are happy if you open your hotel- we are interested in this same topic here, and everybody meets with us, and if you need a meeting, we can set this up for you as well, just go for it, right? So maybe have something like that noted down somewhere, so people feel encouraged doing that.
**Pablo Baeyens** 28:15 I think the two things to sum it up that I see us giving people are, one, discoverability, so, like, finding out that there are people interested about the topic, and then the second one is accessing resources that we have, such as Zoom links. Yep.
**Alolita Sharma** 28:31 Yeah, yeah, exactly. And also, I think it would be good to have the… maybe the end user SIG, or the, you know, can have that anchor into a SIG, right? Like, it's the user groups, or whatever we call them, community groups.
You know, kind of…
**Severin Neumann** 28:50 I mean, it's not only end users, right? I mean, depending on what they're doing, users, right?
**Alolita Sharma** 28:54 But they… but they're not, core tech… Core…
**Severin Neumann** 28:59 Right, yeah, this is more likely.
**Alolita Sharma** 29:01 So, if it's finance, for example, it's a market segment, they are not inventing hotel, they are using it. So, from that definition, again.
You know, you could say it's a user group, because, they are… You know, leveraging the standard and the hotel implementations.
For their use case.
So that's… that's why, you know, the user group idea has been in the industry for a long time.
**Severin Neumann** 29:39 Okay.
**Alolita Sharma** 29:41 Do you want me to follow up with Lucas, to find out… kind of communicate what we discussed today, or… Anybody… or Severin, you wanna… you and I can have a chat with.
**Severin Neumann** 29:53 Well, I mean, I would put that question about, like, what they plan and what success looks like for them on their…
**Alolita Sharma** 30:00 On the issue.
I can do…
**Severin Neumann** 30:02 on the issue.
**Alolita Sharma** 30:03 Yeah.
**Severin Neumann** 30:04 Another part about, like, those… those user groups that… that's maybe worth a… a PR.
To the community repurchase, they're like, hey, this is a thing we are happy to have, right?
And as Pablo said, I think discoverability is maybe also another thing that we maybe find a space where we list them then eventually.
**Alolita Sharma** 30:25 Yeah.
They're two different things, though. Yeah, exactly. One is just… yeah.
One… one is definitely following up with Lucas and Books on these… on this…
**Severin Neumann** 30:35 Pretty… Yeah, and for the other one, let's maybe start an issue and then continue on that async, if this is something we want to continue looking into.
**Alolita Sharma** 30:46 Okay, sounds good.
**Severin Neumann** 30:46 I can… I can put out an issue for that. And Alolita, if you follow up with them on that issue, then yeah.
**Alolita Sharma** 30:52 Yeah, I do.
**Severin Neumann** 30:53 Let's maybe move on to… we have a few more topics.
**Alolita Sharma** 30:55 Yep, that's the one.
Sounds good. Thank you.
**Pablo Baeyens** 31:02 I think I'm the next one. Yeah, so I got access this morning to Codex Security. I was trying it out with, OpenTrenical Collector and OpenTermetry Go.
I think we only have, and I realized this after running these two, access to 5 scans on Codex Cloud, But… A month? Running locally?
**Austin Parker** 31:26 temper.
**Pablo Baeyens** 31:28 It just says 5, not 5 a month.
But, you can run it locally, however many times you want, so I guess we can always… Dude, odd.
Oh, okay, so… you can get early access to the paid version if you get in touch. I'll try and…
**Alolita Sharma** 31:52 Oh, nice.
**Austin Parker** 31:52 Hey, really? You do not.
They really don't.
**Pablo Baeyens** 31:56 They are a bit scared about people using it.
Yeah, I… I went through the ones on the collector.
There's a couple of them that seem reasonable. Unfortunately, this is tied to my personal account, and I had to put in a credit card, so I don't want to keep the passport out to people, but I can copy-paste the things into security reports if… They seem reasonable, I guess.
Or figure out another way to… Attorneys.
Yeah, public.
**Alolita Sharma** 32:34 So, in fact, if you give us some feedback, maybe we can ask CNCF to get an account, which Okay, perfect.
**Austin Parker** 32:43 Yeah, I thought they were… Part of the… Dang, bud.
**Pablo Baeyens** 32:49 If you all know of a way to get, like, a credit card that then I can invalidate, I'd be happy to share the password with you all.
**Alolita Sharma** 32:56 Yeah, yeah, they can pay for it, we should ask, for sure.
**Marylia Gutierrez** 33:01 Or you can just give me your credit card and your password to all your bank accounts.
**Alolita Sharma** 33:05 Thank you.
**Marylia Gutierrez** 33:05 Thank you very much.
**Alolita Sharma** 33:08 Alias. Gonna put them to good use.
**Marylia Gutierrez** 33:14 Sorry.
I only take credit cards so I can buy more chocolates. That is my addiction, so…
**Pablo Baeyens** 33:23 Yeah, I… I posted on the GCTC channel, I don't know… if we want to make this available for repos in some way. If we only have 5, I guess.
Probably the best option is for us to choose what 5 repos, or rather, 3?
**Austin Parker** 33:41 Anybody else?
**Marylia Gutierrez** 33:42 When you do the scan, it says, like, do per repo, can I not do, like, per org?
**Austin Parker** 33:48 Maybe… No. Maybe when we… Go to private. We can screen share and look.
I'm curious what you see.
**Pablo Baeyens** 34:02 Yeah, sure, I can…
**Austin Parker** 34:04 Hey, US Evans.
**Pablo Baeyens** 34:05 join from my personal optome, and we can do it, yep.
**Alolita Sharma** 34:08 A monoripo?
**Severin Neumann** 34:13 Since we wanted to go into a private meeting anyways, do we want to quickly talk about Trask's topic?
**Austin Parker** 34:20 Yeah.
**Severin Neumann** 34:21 Continuing that one.
**Alolita Sharma** 34:22 Yep.
**Trask Stalnaker** 34:24 Cool. So just wanted to check if there's any… I wasn't sure if we have any kind of process that, should be followed for this kind of a thing where… explicitly don't want to create a SIG, or a Slack channel based on, the whole infra… Project Infra. Like, I'm trying to scope this down to be more narrow than all of Project Infra, which we've struggled with.
So, just a new repo.
A set of maintainers, and kind of my thought is it's sort of embedded in the maintainer.
SIG, Maintainer Meeting, Hotel Maintainer Channel.
**Alolita Sharma** 35:16 Yeah.
**Pablo Baeyens** 35:17 reasonable.
**Alolita Sharma** 35:19 Yeah.
**Pablo Baeyens** 35:19 Now, OpenTelemetry Go build tools as a precedent where the GoSeq and the collector seek collaborate together, so…
**Alolita Sharma** 35:26 Yeah.
**Pablo Baeyens** 35:26 standard example of that. Yeah.
**Trask Stalnaker** 35:29 don't really technically have a maintainer SIG. I mean, we… But we have a meeting or virtual.
**Alolita Sharma** 35:36 Refrigerate. Yes.
**Trask Stalnaker** 35:37 God.
Okay.
**Alolita Sharma** 35:41 Fine, though, that's…
**Trask Stalnaker** 35:42 As long as there's no…
**Alolita Sharma** 35:44 Go ahead.
**Trask Stalnaker** 35:44 I will, post also in the maintainer and share with the GCTC, just to check if there's thoughts before, moving forward.
**Marylia Gutierrez** 35:57 And if you need help creating, like, the team and the repo, just let me know. Traskat can also help out.
**Trask Stalnaker** 36:05 Awesome, thank you.
**Alolita Sharma** 36:11 So, Trask, is there a limitation of, who can be a code own… in the code owners? That is, they have to be maintainers, right, of hotel?
In some sink? Or the other?
**Trask Stalnaker** 36:23 I would say that probably it should be limited to approvers and maintainers from existing SIGs.
**Alolita Sharma** 36:31 Okay, yeah.
**Trask Stalnaker** 36:32 It would require a maintainer to sponsor a new shared workflow.
**Alolita Sharma** 36:39 Okay.
Makes sense.
**Trask Stalnaker** 36:42 Yeah, yeah, we… the bar should be… Fairly high on the repo, given the sensitivity of sharing workflows.
**Marylia Gutierrez** 36:51 Yeah.
**Alolita Sharma** 36:52 Yeah.
**Marylia Gutierrez** 36:52 I was gonna say the same, like, this level, like, scrutiny of everything get added would definitely, like.
check for a lot of things before we put in anything, because we're gonna get installed, and then people.
**Alolita Sharma** 37:03 Yes.
**Marylia Gutierrez** 37:03 Optin, so, definitely would have to be very careful.
**Alolita Sharma** 37:08 Agreed.
Yeah, I mean, I think, that's a good thing to call out.
**Trask Stalnaker** 37:18 Buh.
Should we go… Open the private meeting.
**Alolita Sharma** 37:25 Yeah, sounds good.
**Austin Parker** 37:27 Yeah, let me…
**Alolita Sharma** 37:28 He has a link.
**Austin Parker** 37:29 I'll start one and put it in the chat.
**Alolita Sharma** 37:31 Okay.
**Trask Stalnaker** 37:32 Thank y'all.
**Alolita Sharma** 37:32 Sounds good. See you.
