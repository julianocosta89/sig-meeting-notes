SIG: Governance Committee
Date: 2026-04-01
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/kCFNu3JJvUBdxt77R44F9oRLDlhQ2730RMKk3HpKmSFqoGNLS5G7pULAX387nfeI.mUtUYy72C6Q3Zt9E
============================================================

## Zoom Recording Transcript

**Marylia Gutierrez** 01:07 Hello!
**Trask Stalnaker** 01:08 Hey, Marillia.
**Marylia Gutierrez** 01:11 Hmm, how are you?
**Trask Stalnaker** 01:13 Doing good.
Welcome back.
**Marylia Gutierrez** 01:16 Okay, thank you.
**Trask Stalnaker** 01:19 Fun to see photos.
**Juraci Paixão Kröhling** 01:37 Hello, hello.
**Trask Stalnaker** 01:40 Hey, Jossie.
**Marylia Gutierrez** 01:42 Hello.
So, Jessie, since I couldn't make my joke about deprecating collector on the talk because of possible riots, I… I just made, like, a joke today on LinkedIn. I posted, like, which of those would create more riots? So I included the deprecation of the collector there.
Yeah, tracks that they didn't.
**Juraci Paixão Kröhling** 02:22 Let me do that.
**Marylia Gutierrez** 02:22 I wanted to have the whole update about hotel, and when we are about to leave, I was just gonna say, oh, by the way, we are deprecating collector, and let's just leave the stage.
Just see.
**Juraci Paixão Kröhling** 02:33 Yeah. The other option would be, we are rewriting the collector in Rust, but then, I guess, That would be an even bigger problem.
**Marylia Gutierrez** 02:45 So, yeah, for my own safety, it was decided that…
**Trask Stalnaker** 02:51 I like that you're prioritizing safety.
**Marylia Gutierrez** 02:53 Yes.
**Severin Neumann** 02:57 Hi there.
**Marylia Gutierrez** 02:59 Hello.
**Trask Stalnaker** 03:00 Hey, it's everyone.
**Juraci Paixão Kröhling** 03:08 I have to say that I'm a little bit disappointed by the April Fool's pranks so far.
So, yours was okay, Marina, but I saw some that looked like real announcements, and perhaps they were.
Like, real announcements?
**Marylia Gutierrez** 03:23 Yeah, it's always tricky. I feel like a lot of times, people, like, I have this idea, I don't know if it is good or bad, so I'm gonna post it today, and if people, like, roast it, I was like, haha, no, it was a joke.
**Juraci Paixão Kröhling** 03:35 Oh, Gmail started like that.
**Marylia Gutierrez** 03:38 Myths?
So yeah, I share here all my awesome ideas.
**Juraci Paixão Kröhling** 03:52 Nice. Oh, 3 minutes ago, okay, yes. Nice.
Yeah, I shared one today.
That we are doing.
a partnership with Dash Zero on observing portlets, like JSR286, for those who know.
Like, I was a portlet developer, and merko was also a portlet developer.
**Trask Stalnaker** 04:19 That's wild.
**Juraci Paixão Kröhling** 04:20 Oh, it would be.
That got some memories from you, didn't it, to ask?
**Trask Stalnaker** 04:26 Yes, yes.
**Juraci Paixão Kröhling** 04:28 Yeah, I was… I remember being excited for, like…
**Trask Stalnaker** 04:31 10 minutes about that.
**Juraci Paixão Kröhling** 04:33 Oh, really? No, I worked at 3 years on that, so… I was a developer for Gate In at JBoss at Red Ahead back then.
I was responsible for WSRP, like the, I even forgot what that stands for, but that's remote server, remote, remote portlets, basically, so you could load remote portlets into your portal, so yeah.
**Trask Stalnaker** 04:57 Yeah.
**Juraci Paixão Kröhling** 04:59 That was fun to debug.
**Trask Stalnaker** 05:06 Oh yeah, I would have been more, I just… I don't think I had any… I remember looking at it and being like, how can I use this? How can we integrate this into our product? And I didn't… Come up with anything, so then moved on.
**Juraci Paixão Kröhling** 05:23 So there were banks in Germany that they were using portlets for their internet banking.
Even after we stop supporting portlets. So, yeah.
**Trask Stalnaker** 05:34 There are… Well, as we saw, there was somebody still using web objects, Recently.
**Juraci Paixão Kröhling** 05:45 Yeah.
Yeah, that's something that I also worked with before.
And it was fun, it was actually cool back then.
200, what, 3? 2? Yeah, that was fine back then.
**Trask Stalnaker** 05:59 Oh, I was… I was doing it in, 1998.
when…
**Juraci Paixão Kröhling** 06:06 It was…
**Trask Stalnaker** 06:06 Objective-C, and they had a Java shim on top of it.
And it was a nightmare.
**Juraci Paixão Kröhling** 06:16 No, but that's, that's what I've done as well, but that was 2002 or 3 or so, yeah, but no, not 1998.
**Trask Stalnaker** 06:23 I only remember, because that was my first… my very first job.
**Juraci Paixão Kröhling** 06:29 Jace.
No, I was doing parole back then.
**Trask Stalnaker** 06:39 Perl is way more sane than Objective-C bridging.
**Juraci Paixão Kröhling** 06:44 True.
**Trask Stalnaker** 06:45 Oh, I got the memory leaks that came through that, bridging process.
It's a nightmare.
**Juraci Paixão Kröhling** 06:54 What is funny is that is the predecessor of Ruby on Rails, right? I mean, a lot of the ideas behind web objects, they influenced, or at least looks like they influenced Ruby on Rails.
Like, the active record pattern.
**Trask Stalnaker** 07:09 That's hot.
**Juraci Paixão Kröhling** 07:09 Straight from web objects.
**Trask Stalnaker** 07:12 It was very… I mean, it was way ahead of its time, yeah.
**Juraci Paixão Kröhling** 07:19 We are showing our ages here.
**Trask Stalnaker** 07:20 I can't hide my age.
**Juraci Paixão Kröhling** 07:29 All right, so I think we have Coral now.
**Trask Stalnaker** 07:31 Hey, yes!
**Austin Parker** 07:32 Hi! Yes, hello.
**Trask Stalnaker** 07:34 Hey!
**Marylia Gutierrez** 07:35 Hello.
**Juraci Paixão Kröhling** 07:39 Alright, folks, I do have something to share.
Let me look at the agenda.
Okay, that's… Oh, we actually have a few things there. No, we don't.
Okay, cool, we don't.
So, I promised to add this to the agenda.
Afterwards, but one thing before I forget.
I… you all probably know that I organize hotel night here in Berlin, every couple of months, like, whenever I have time, whenever I… like, there is a place, there are people, I… I just do it in my capacity as a CNCF ambassador.
there are a few rules that I do, that I follow, like no vendor pitches, No vendors at all, whenever… Whenever possible.
So hosted at end users, and talks by end users, and things like that. So there are a few principles that I try to follow.
I've done something similar in Sao Paulo a few weeks ago.
And and a few people from other places, they started pinging me and saying, oh, I'd like to have an hotel night elsewhere as well.
During KubeCon, I had a conversation with, other people, including people from the CNCF, like Audra.
And there is this wish to do global hotel nights.
again, meetups, not conferences, not full conferences, following the same philosophy that we have here in Berlin.
And, I'm not… I don't know if I'm ready to take the, like, the next step there.
But I… I do want to run it through the GC before making it Even a tiny bit more official.
than what it currently is. Like, it is not official at all, but if it is going to be something hosted by the CNCF in some way, even if it's more than just a… the events page.
then, then I think I'd like to have a… at least They should see knowing beforehand, before anything is made public in that sense.
So to… To recap, the idea is… doing global hotel nights, following the same pattern that we have here in Berlin, so no vendors, hopefully, at least that's the main rule that can be broken from time to time, and expanding slowly to other, geos. So the next one, or a tentative one, could be Amsterdam, so we have people there that want to host and want to talk.
And New York.
we have a space, we have speakers also for New York, ready? Like, people… we were just discussing this idea, then suddenly we see himself ambassador passed by, and turns out, he's, a, he's an end user, he has a space, and he was in, like, right away.
Lolita is not here, but she also mentioned that she would be in for the one in… in Cupertino, like, Bay Area, or whatever, like… So… there is an interest. And, before… Investing any more time there.
I'd like to hear any concerns you may have. Like, if you do have concerns.
I'd like to talk about it. Otherwise, I'll just try to do it on a separate thread, like, background thread from my… And having… People around me helping in organizing those events.
And yeah, Morgan, tell, tell them that I am still waiting for their email, with the proposal, like, the abstract and the title.
I sent them the message yesterday.
But yeah.
I will tell. So, any concerns?
What is it?
**Morgan McLean** 11:26 Sorry, hunting for the mute key. I will tell them that right now.
**Juraci Paixão Kröhling** 11:29 Okay, cool, yeah.
Cool, any concerns, folks? Any reasons I should not be doing this, other than… Finding time where I don't have… Okay.
Then.
**Morgan McLean** 11:54 Yeah, I got nothing. I was gonna say, I have no concerns, this sounds really good, duh.
**Juraci Paixão Kröhling** 12:03 Alright, so, the next step is then… To formalize this as a pull request.
in one of the SNCEF repositories. This is on me.
for… like, for, if you don't know, the rules that I have is mostly what I've shared.
but also… Every couple of months, we… we would hope to do one of those And, whenever we have a vendor, then ideally two vendors, so that one can do a counterpoint to the other.
We had something similar here in Berlin for eBPF, so we had Grafana and Odigos at the same day, at the same place, talking about the same thing, so they could One level the other.
And, it says… oh, yeah, and .
**Trask Stalnaker** 12:54 How… do you think that's an important… Thing to allow.
**Juraci Paixão Kröhling** 13:01 I think so… I think I'll prefer to be strict at the beginning, and then break the rules whenever we need.
Especially at the beginning, I think it's not going to be a huge problem, like, there's a suppressed demand.
For that, so, like, a lot of people wanting to host, a lot of people wanting to talk, so I don't think we need vendors in the beginning.
But for recurring events, like, look, recurring, hotel nights in specific locations, then there might be a case where we don't have enough speakers, and then we can step in and invite one of the vendors there.
this situation we have right now in Berlin, like, for the April 14th, right? So we are having somebody from Splunk, And, we're having also Delivery Hero, basically doing the same talk that they've delivered last week, at KubeCon.
So I think the rules are there, like, more like a guideline than… than… Concrete rules, or, like, strong rules.
But I'd prefer to be conscious about breaking them instead of just letting people do whatever they want.
I don't want Hotel Night to be a vendor show.
I think that's the main… the main idea for the… for the event.
The other role is those who organize don't speak, so I try not to speak at my own events. Also.
Because I don't like the idea of, like, having 5 organizers and 5 talks from the same 5 organizers, that's… that just doesn't feel right.
But all of those rules are going to be part of this pull request that I'm opening with the CNCF.
**Trask Stalnaker** 14:45 Cool.
**Juraci Paixão Kröhling** 14:45 Cool.
Right?
So… Austin, I think the next item is yours. Now we have an agenda.
**Austin Parker** 15:09 Yeah, I just wanted to update people real quick on graduation.
We are… Still playing the waiting game with the second round of adopter interviews.
They've also lined up… a doctor interview with the New York Times, I believe?
Who identified themselves.
But…
**Morgan McLean** 15:40 I think… things may have changed. I believe they're a Google Cloud Ops customer using OpenTelemetry.
**Austin Parker** 15:46 Okay, yeah.
Either way… The, you know, the… the word I got is… we're just kind of waiting for the paperwork to finish up, and then they'll have a vote, and… The recommendation seems positive.
Yay.
So… Mostly, it's just getting the adopter interviews done.
And yeah, that's… that's all the news that's hit to print about graduation.
Do I have the next thing as well?
**Morgan McLean** 16:30 I was gonna ask, Austin, like, last time we were up for graduation, there was concern that they had not actually reached out to the groups we were asking them to interview. Is that… is that different now?
**Austin Parker** 16:39 It's different. Yeah, no, we've confirmed… we've confirmed that the people that We're on the lists are the ones that have been… Contacted and…
**Morgan McLean** 16:50 records. Okay.
**Austin Parker** 16:51 Yeah.
**Morgan McLean** 16:52 That's fantastic. Thank you.
**Austin Parker** 16:54 So… So my second point… I… So this is a little bit of a, like, readout from the GenAI SEMCOM chat at KubeCon, and also just sort of a… generic question.
But it's around GenAI, SimConv, and sort of the proliferation of SEMCOM-shaped things that are out there.
there's… The first point is one of the things that we discussed at the GenAI STEMCOM meeting was the idea of… Creating some sort of… like… Fast.
Bass, some kind of? I don't quite know, I don't… like, Lamila might remember better than I do, but the… The basic concept was, like, okay.
over here is sort of a set of instrumentations and simcoms and stuff that we're committing to, like, a monthly release cycle on.
That if you are a vendor, you're building something in a space, or whatever.
You can kind of… this is where you can come in, and it's not gonna take 6 months.
to… release it. Now.
just because something is in, sort of, the fast ring doesn't mean it's going to be promoted to the, like, main SimConv. There's still usual stability stuff that goes through there, but… There's at least the thought of, like, trying that, And then also, or concomitantly.
Going out and sort of making a public statement as a project of, like, hey, there's only actually one Gen AI, semantic conventions, and… these are the only two ways, you know, these… you either have the normal one, or you have the fast one, and that's it. And anyone else that is saying, we have… semantic conventions… Like, they are not official OTEL semantic conventions.
And that's kind of… that second part is more of what I wanted to get the GC take on.
**Morgan McLean** 19:33 I'm basically, like, making a public statement, drawing a line in the sand.
These are not official.
**Austin Parker** 19:39 Right.
**Morgan McLean** 19:40 Yep.
**Juraci Paixão Kröhling** 19:43 So, is this… The thing that… Are we being concrete about names here, or are we avoiding names because we're being recorded?
**Morgan McLean** 19:58 I don't think we can have a real discussion without names. I don't think we need to worry about being recorded.
**Austin Parker** 20:02 Yeah, I mean, I think there's… there's several different… Things here, right?
**Morgan McLean** 20:08 Right, there was the Microsoft thing that you found, or the Microsoft Cisco one. There's also, like, open LL Emmetry and others.
**Trask Stalnaker** 20:14 That's what I thought.
**Austin Parker** 20:15 inference.
**Trask Stalnaker** 20:16 4 months ago, that Microsoft thing, I don't think that's an anything burger.
**Austin Parker** 20:23 I… I mean, I don't.
**Morgan McLean** 20:24 Fulton.
**Austin Parker** 20:25 The thing is, is I don't… I also agree, I don't think it's anything, or I don't think it's, like.
I'm not… I don't think that… I'm not making a moral judgment, right? I don't think this is, like… I don't know… I don't know why this happens. I… I can… I can say, okay, open inference or open LLMetry, that at least is a slightly more clear, like, why did this happen, and why did it happen this way?
Because of other things.
But for, like, this Microsoft Cisco thing, it's like, who knows? Like, I'm sure there's a PM at Amazon right now coming up with… OTO-compatible… Semantic conventions for their agent stuff, if they haven't already done that.
**Juraci Paixão Kröhling** 21:13 So, that's actually why I'm… I'm asking that question. So if… if we are talking about one specific situation that, was discussed, I think, a couple of weeks ago.
then I do know that, one of those proposals, they came from people who are not very familiar with how OpenTelemetry works as a community.
And they just try to do something on their own.
And I'm talking to them and trying to get them closer to us.
And do that here.
Right, so… not being concrete here, because I think we're not being concrete, but I can share the name of the… of what I'm talking about here in the chat.
But, So in that case, I think it is kind of sorted out already, like, it's in a good path, to fix itself eventually.
But if there's more to that, then… then definitely we need to, I think.
I would support having a public blog post.
not specific to Gen AI, but perhaps using GenAI as an example.
And perhaps even calling back the example from Elastic, like, oh, it is so important to have one standard that even Elastic donated their common schema to OpenTelemetry, because it's important to have, like, one source of truth for telemetry schema.
**Austin Parker** 22:35 Yeah, Trask…
**Trask Stalnaker** 22:37 Yeah, my perspective on why this… I mean, one of the reasons why this happened, has happened… Is that… And the area where I want to focus our efforts is on making our GenAI semantic conventions and instrumentations They have not been, They have not gone fast, and they have not been the… like, if they were early and really good.
then, you know, I don't think we would have had so many Other pieces come up, but… People, you know, started their projects a year ago, say, or longer ago, before there were certain semantic conventions. I don't know if you saw that somebody opened a spec pull request, a couple weeks ago to introduce, like, a whole lot of GenAI semantic conventions, and I had gone through it, and almost all of them have been added to GenAI semantic conventions in the last 6 months.
So, like, a lot of things have picked up in the OpenTelemetry GenAI semantic conventions, it's just taken us longer because of our general pace.
And… I think it's matched our pace of other semantic conventions.
even faster, probably, than our general other semantic conventions and, instrumentation's kind of on par. It's just that this is a space that's moving very fast, and people want to move fast, and so they… if they don't see the solution there, they just build it.
So I mean, I feel like if… we focus… I'm not sure we need a statement that says, like, there is one true GenAI semantic conventions. I mean, from the big picture.
we want, you know, I mean, this idea of federated, of, like, you know, people can do their own semantic conventions.
But… I feel like that problem will naturally solve itself if we… can solve our own, kind of, our own house, or get the… I mean, there were a lot of good ideas. Lyudmila shared with the GenAI SIG yesterday the discussions that were had at KubeCon.
And there's a lot of good ideas there.
I think we can make that… SIG and the semantic conventions, and the Python instrumentation, in particular, move Faster and be more, successful.
So that's kind of… I'm not sure we need… I feel like if we can get those things successful and fast.
Then these other things will sort of naturally in a way, like, peter out, right? Like, there's gonna be, like, a long tail of, like, okay, I'm tired of maintaining this other thing now that there's a, you know, there's a good open telemetry story around it.
**Morgan McLean** 26:13 I generally.
**Austin Parker** 26:14 Yeah.
**Morgan McLean** 26:15 agree with that, like, I've… I've heard the same feedback in… well, I've heard the same feedback to a degree, internally, from, like, Cisco teams.
and even teams within Splunk that are trying to work in the Gen AI space that, hey, you know, they want cement to conventions now, they need something to work with right now, their customer's demanding things, it's going to take a while to do it in OTEL. I do think if we're able to speed things up inside of OTEL, that will help a lot, whereas you say, a lot of those other initiatives will just sort of fizzle out.
at the same time, some percentage of the feedback is when I ask them, like, oh, did you actually try and work within a hotel? They didn't even join a meeting, right? Like, it's just… for some of them, it's just the excuse. It's the… it's the rationale for just going their own.
**Trask Stalnaker** 26:52 Oh, it's so much easier just to tell AI to generate some submissive to do.
**Morgan McLean** 27:00 Yeah.
**Austin Parker** 27:01 And that right there is why I do think… I mean, I'm fine… I don't think we need to say, oh, there's only one true sin count, right? But I do think… I think we need to message a little bit about this, and just kind of… and say, like, you know.
For example, Maybe, maybe the way we phrase this is.
hey, we're gonna be doing something, you know, we're gonna be doing this that is, like, a faster, you know, more experimental, you know, whatever, right? We're gonna… here's some changes that we're making to how we iterate on semantic conventions, so we can kind of point people to that and be like, look.
here you go, right? Like, here's… This is working, this is operating at your pace now.
But we do need to have that marker out there of, hey, You can't ju… you know…
**Morgan McLean** 27:54 You can't claim… Zero, if they're not.
**Austin Parker** 27:57 You're gonna…
**Morgan McLean** 27:58 Yeah.
**Austin Parker** 27:58 If it's… if you're not actually, like, doing OTEL, then you're not doing OTEL.
Yeah. And we're gonna have more… Like, at some point in the future, we will need… like, one of the things that we got that came up at… KubeCon as well, was conformance, And… you know… Post-graduation, I think a big part of what we're going to wind up doing is figuring out what does conformance look like for this project.
And I think that… CENCOM is gonna have to be a huge part of that. So, I do think it's good for us to kind of start drawing these, like.
lines, almost, and being like, look, you know.
not you're on one side or the other, but hey, this is the stuff that… like, I think you're… yeah, this actually is a great example, Trask.
Yeah. Like, I think just being able to have something like this generated, and just, like, on the website or whatever, and being like, hey, this is… this is the source of truth.
**Morgan McLean** 29:10 Yeah.
**Trask Stalnaker** 29:10 Did you see anything?
**Morgan McLean** 29:11 extending is that it's not necessarily OTEL, right? It's OTEL plus some proprietary stuff.
**Austin Parker** 29:15 Right, it's hotel plus some proprietary stuff. And we don't… and we can be like, hey, if you want to do proprietary stuff, which is fine, that's on you.
**Morgan McLean** 29:21 Yeah.
**Austin Parker** 29:21 But… but if you're gonna say, hey, we're doing OTEL, Mmm, no, you… like…
**Morgan McLean** 29:27 Yeah.
That's the issue. Yeah.
**Austin Parker** 29:29 Yeah.
**Trask Stalnaker** 29:37 Yeah, so these… I think conformance is, a really… could be a really good way for us to drive for all… for all the Light, all the instrumentations.
Because as a… as a vendor, with my vendor cap on, I actually don't care that much whether the instrumentation is hosted by… written by OpenTelemetry or somebody else, as long as they're emitting the… Semantic conventions.
That then my dashboards display.
Yeah.
I think long-term, although I guess I do care in the sense of, Long-term stability for my customers is going to be better, if the instrumentation is community-owned.
**Austin Parker** 30:35 Damn.
**Trask Stalnaker** 30:36 And under the community governance.
I love my…
**Austin Parker** 30:41 Imagine.
**Trask Stalnaker** 30:41 I mean…
**Morgan McLean** 30:42 Not to mention, as a vendor, your cost will be lower, right? Because, like, otherwise you're committing to maintaining this stuff forever.
**Trask Stalnaker** 30:52 So, Austin, I like the… I mean, the idea, like, I totally agree with… Should make noise, sort of, about… our efforts in the Gen AI space, because I think that As sort of witnessed by that spec PR that was opened up.
Where somebody would… had no… was not even aware that we had added all of these new GenAI semantic conventions.
**Austin Parker** 31:25 Yeah.
**Trask Stalnaker** 31:26 that… So… Yeah, and we do really need I mean, all of this takes a lot of effort in the GenAI SIG, So really appreciate, Sending Jamie our way, and, anybody else…
**Austin Parker** 31:46 should be…
**Trask Stalnaker** 31:48 that…
**Austin Parker** 31:48 Yeah.
**Trask Stalnaker** 31:49 Thank you all.
**Austin Parker** 31:49 We have people coming in…
**Trask Stalnaker** 31:52 can send into the GenAI SIG will really help us. I really feel for… Lyudmila has been driving that on her own for so long, and it is a challenging space.
**Austin Parker** 32:11 Yeah.
**Trask Stalnaker** 32:11 essence.
**Austin Parker** 32:13 Yeah… Yeah, yeah, yeah, yeah.
I… yeah, I think… I mean, I don't want us to be… I don't want the GC to be prescriptive about, like, exactly how that, you know, the SEMCOM figures out how to do it.
I do want the GDC to be prescriptive about, like, making noise about it.
And… signaling to… you know… Both signaling to other vendors, signaling to, sort of, your… your… Foundation Labs signaling to everyone, it's like, hey.
We would really like you to work with us here, like, I'm… I'm gonna be in New York tomorrow for… MCP Dev Summit, and there's gonna be, you know.
like, there's this whole Agentic AI Foundation now, and Linux Foundation, and we obviously talked to some people last, you know, two weeks ago about that.
So, just like… Right, like, I think we need to make sure that we're kind of directing people into these community channels that are better suited to, sort of, steward these things long-term.
And part of that is just communicating that, hey, yes, that's what we are… look at the stuff we're doing with these other people.
Alright.
That was all I had on the Gen AI stuff.
**Severin Neumann** 34:00 I just added one more topic to the agenda. I mean, I shared it before, like, just wanted to let you know once again, like.
We start this Bloomberg mentoring thing next week, officially.
So April 8th.
They have lined up, like, something between 30 and 45 engineers. Interestingly, a lot of them already have experience with OpenTelemetry and are really eager.
To contribute, so yeah, let's see what comes out of that.
There was also an announcement on this CNCF blog.
Yeah, if you have any questions, or if there's anything… And then we can chat about it, but that's more an FYI.
**Trask Stalnaker** 34:46 Cool.
**Severin Neumann** 34:48 Anything else?
Any other topics?
**Austin Parker** 34:51 Talk about how KubeCon went?
**Morgan McLean** 34:53 Yeah, I was about to say, I ended up having to cancel last minute, but how was it?
**Juraci Paixão Kröhling** 35:01 I'm.
**Austin Parker** 35:02 Hey.
**Juraci Paixão Kröhling** 35:03 The project updates were, it was packed.
Easy? Was that the word that he used?
**Austin Parker** 35:10 Busy. Biz. Busy.
**Juraci Paixão Kröhling** 35:12 Oh, busy! Okay, I'm sorry, yeah, I heard easy, and I was like, oh, wait, only for you.
**Austin Parker** 35:16 For me, it was remarkably easy.
I just said… I got to point, Adrian, on recent problems instead of having to deal with that myself.
**Juraci Paixão Kröhling** 35:25 No, it was…
**Marylia Gutierrez** 35:26 I felt like it was a lot of, like, interest in hotel, like, in general. You can see, like, the sessions about hotel were usually, like, pretty full, and people, like.
Talking about it, like… hallway track kind of thing, yeah, so even, like, the rooms that we got for some of the talks were also, like, quite big, so…
**Austin Parker** 35:45 Yeah.
I think we, new record for Observ… I feel like new record for Observability Day, too, where our, like, biggest session had, like, 540-something people?
**Juraci Paixão Kröhling** 35:57 That was the opening session, so that's kind of expected, but yes.
**Austin Parker** 36:01 Still, they could have gone to any other opening session.
**Juraci Paixão Kröhling** 36:05 Right, yes, that's, that's true. Yeah, I mean, two of the top, attended, sessions were around OpenTelemetry, so I realized.
**Austin Parker** 36:15 I do.
**Juraci Paixão Kröhling** 36:15 Jared at Wall Street? Those numbers are the names.
**Austin Parker** 36:18 O.
I mean, I think he goes in there, I think they officially, publish it in the transparency report.
**Juraci Paixão Kröhling** 36:27 Okay, but .
**Austin Parker** 36:29 We'll talk about it on this call.
**Juraci Paixão Kröhling** 36:30 Yeah.
So among the top, talks for observability today.
OpenTelemetry was among the top, right? So I think this is clear for at least two of the top talks are about OpenTelemetry.
So observability Today, I feel like it was… On my book, it was a success.
I don't know much about the… the Project Pavilion booth, I unfortunately… didn't even go there. I'm not proud of it. But I think next time, We're gonna have, We are gonna try to do another observatory. Morgan, blink, blink.
So…
**Austin Parker** 37:11 Just, just…
**Morgan McLean** 37:13 Mr. Clark, you said you do want one, or you don't?
**Juraci Paixão Kröhling** 37:15 So, let's have a conversation with the community managers. I think the general community wish is to indeed have one.
**Morgan McLean** 37:24 Okay.
Easy enough.
**Juraci Paixão Kröhling** 37:26 Everybody that we talk to from the community, they say they want.
Community managers, they also want.
The one thing that people are kind of, like, Matt, it's like, with the name on the map, it being, Cisco or Splunk.
**Morgan McLean** 37:42 I want to change that, too. So, like, just to be clear, the name on the map was not our intent, that's the CNCF doing it.
**Austin Parker** 37:48 Yeah, the.
**Morgan McLean** 37:48 I do not want it to look like that. Yeah.
**Juraci Paixão Kröhling** 37:51 That is the problem is…
**Austin Parker** 37:52 Problem.
**Morgan McLean** 37:53 Yep. Like…
**Austin Parker** 37:56 I… I'm gonna defend the community… the pavilion booth, like… We did get quite a bit of traffic, I feel like. The… I understand… the downside… Definitely, it's worse for, sort of, the SIGs having their meetings.
Like, that was obviously worse than it was when we had the observatory.
Just, there's less room, it's… Well, I guess it's about the equal… actually, it wasn't that noisy over there. One nice thing is that the pavilion was kind of off in a wing, and it was pretty… like… You didn't have to shout, which… the main floor, where all of the activation zones were, was actually, like, super packed. And… Would have been significantly louder and harder to have meetings there.
But… There are other, like… Like, I think there's thing, you know.
I think if we wanted to… work with… LF projects on… Like, having meeting space, or having a room, or having, like, a section where we could do those project meetings, those, like, SIG meetings.
Because Kubernetes does do this, they have, like, a whole…
**Severin Neumann** 39:17 That's the thing I wanted to comment on. So, Kubernetes has this meet and greet area, and I saw it. I'm not sure if anybody of you saw that.
And by accident, I talked with someone from CNCF about it, like, we passed it, like, we were talking, and we passed it in as a, like, hey, why can't OTEL not have something like that? And the answer was, like, I don't know, maybe they can. So, I mean, especially if we…
**Austin Parker** 39:39 We've never asked.
**Severin Neumann** 39:40 Yeah, yeah, so… and I don't know, was this meet and greet thing from Kate's, like, a new thing? Like.
**Austin Parker** 39:47 No, they do it.
**Severin Neumann** 39:48 They're having it… They get it every year?
**Morgan McLean** 39:50 Just because they're big, or does someone pay for it, do we know?
**Austin Parker** 39:54 No, it's just…
**Severin Neumann** 39:54 No, no, this was an official thing, right?
**Austin Parker** 39:57 No, they…
**Severin Neumann** 39:58 It's supposed to… yeah.
**Austin Parker** 39:59 They do it every year.
It's… it's usually… They'll… they'll put it somewhere. This was, usually it's actually in a… Conference? Or it's, like, in a meeting hall, or, like… it's usually not, like… like, this was one of the more exposed ones. There was, like…
**Morgan McLean** 40:22 Maybe in, like, a hotel attached to a conference center or something, usually, that's what you're saying.
**Austin Parker** 40:25 No, it's always in the conference center, but it's usually, like, in a… in a place that they would do a talk, but they set it in, like, rounds.
Yeah. And then every SIG gets, like, a, you know, a little standee at their table, and then everyone kind of comes and… Hangs out. Like, I totally think we could do that. Like, I think we would just need to ask.
I think, yeah, my two cents is if, I think there's a lot of… advantage… I think… I don't know. I generally feel like it seems unlikely that we are going to solve the, like… The generic problem of, like, whose name gets on it, because that's just how the sponsorship stuff works.
And… It would be better for the long-term health of the community to go through the proper channels.
But, Maria, you've had your hand up, sorry.
**Marylia Gutierrez** 41:34 Yeah, so I was gonna bring, like, two points, I think, like, one, because I just want to give, like, explanation for the ones that did not attend. We got lucky with a position, because the project pavilion was, like, several rows of projects.
And hotel was on the last one, and after that, we had the tables used for lunch.
So we took advantage of those tables, and we just kind of took ownership, but if our booth was, like, in the middle, I think it would be a little harder, because people didn't have a place to stay. So, in that sense, we got lucky, because the first day we could actually, like, we took a few tables, and then the rest of the days, people were just, like, knew that those were the tables that we were hanging out, so they were always busy, like.
people that are contributors, but also, like, some people that are, like, end users and would come and ask questions, so I would try to hang out on that area from, like, time to time as well, so it was always busy. But I think we got lucky with the position.
And the other thing was… Yeah. The other question was, like, about, like, the naming. So, I know the other thing that's… Ted was working on is having, like, an account for, like, hotel that can be used for, like, events. Maybe we can use that as, like.
the sponsor of the observatory, so this way, even, like, for example, like, okay, Splunk's gonna help out, they're gonna put, like, the money on the account, but it's the GC account that would have the observatory, so the name would be, I don't know, hotel, or something like that.
**Austin Parker** 43:04 Damn.
**Marylia Gutierrez** 43:04 So maybe that is one of approach?
**Austin Parker** 43:07 There… I did get some friendly advice that we… Not pursue the open collective thing.
But I also got some… yeah. I also got some interesting… just an interesting note is that… Due to… changes in patent law, or… For legal reasons, it might be in the future that CNCF projects actually become LLCs unto themselves.
**Morgan McLean** 43:44 That was so…
**Austin Parker** 43:45 Open Collective, which would solve a lot of problems. I don't think it's specifically about Open Collective in general, I think it's specifically about Aforementioned legal things.
**Morgan McLean** 43:54 Okay, okay.
**Austin Parker** 43:55 Because… cuz, keep in mind, hotel… is… we… the nine of us, remember, we don't own OTEL. You know, the only legal ownership of OpenTelemetry is through the CNCF.
But… in a future where there is OpenTelemetry LLC, and the GC is, like, the board of OpenTelemetry LLC, That does sort of change the calculus in some of this stuff. But, you know, that's not a thing that's gonna exist by… this fall.
Ultimately… Yeah.
I think Adriana and Reese and… I think the community managers, you know, should have the final decision, but… I do think that… Long-term, it's better to kind of… Like, it doesn't really… I don't know, like… It's a nice-to-have thing for us.
For maintainers, but are there other things that sponsors could spend that money on that would be nice for maintainers?
Like, sending more of them to the conference to begin with.
**Morgan McLean** 45:30 How was turnout, speaking of that?
For hotel maintainers.
**Severin Neumann** 45:36 I mean, there were a lot of maintainers.
**Austin Parker** 45:38 There were a lot of…
**Severin Neumann** 45:39 containers, so it's… it's hard to.
**Austin Parker** 45:41 Yeah.
**Severin Neumann** 45:42 I think there were, let's say, 20 maintainers, maybe, but we have 100-something, so… I don't know, like…
**Austin Parker** 45:49 felt… About the same?
I think part of the issue is that for a lot of people, especially now with, With travel budgets, and with, you know, things being what they're… what they are.
Like, if you don't get a talk-in.
You're not getting the, you know, you're not getting your travel paid for.
But I do wonder if, you know, as a hypothetical.
Would some of the, you know, instead of spending however much on the observatory, would people be willing to say, like, oh.
We're gonna put that money towards something where we can sponsor a maintainer, to go…
**Marylia Gutierrez** 46:42 Yeah, I was gonna say, in total, we have 150… maintainers. We have 328 people with any status, triage or maintainer, or approver.
**Morgan McLean** 47:03 Any other feedback from KubeCon?
**Juraci Paixão Kröhling** 47:11 Yeah, yeah.
**Austin Parker** 47:11 I have a…
**Juraci Paixão Kröhling** 47:14 People know about semantic conventions?
So people know about semantic conventions, but they don't know how to use it.
like, one question that I like to ask nowadays is, do you know about semantic conventions? And people are very happy, yes, of course I do. Can you confidently say that your company is using semantic conventions correctly? And they say, no.
Of course not.
But I think Weaver is gaining traction there. So whenever I talk to people about semantic conventions and going in this direction.
they… and if they know about Weaver, they are very interested.
If they don't know about Weaver.
Then they get interested by the problems that we were solving.
So, I think Waiver is very promising.
**Austin Parker** 48:03 Yeah, a lot of… Definitely saw more, kind of, talk about Weaver.
I thought the… Prometheus and… Hotel meeting at Maintainer Summit was good. It was very short, but it was good to at least get a bunch of people, like, talking to each other.
**Juraci Paixão Kröhling** 48:28 Was it on Friday?
**Austin Parker** 48:30 It was on… Sunday…
**Juraci Paixão Kröhling** 48:33 Oh yeah, okay, so the… yeah, yeah. No, the maintainer summit thing, right?
**Austin Parker** 48:37 Yeah.
**Marylia Gutierrez** 48:39 So that one… It's, like, a little weird, because, like, we have, like, the topics, and for example, a lot of people voted to talk about, like, the SDK, and then I saw, like, okay, nobody from, like.
the SDKs were, like, on this table, so I sat, and then a couple people joined, and nobody from Prometheus joined at that table. So, it was just, like, okay, then?
**Austin Parker** 48:59 Yeah, people were very interested in entities.
**Marylia Gutierrez** 49:02 Yeah, because, yeah, I saw that side of the table, I was like, okay, we have too many people there, I'm gonna help on the SDK one. So we basically spent the time just, like, seeing how many like, SDK have, like, exporter, like, amount of downloads that people are using, if there were opening issues, we'd kind of, like, didn't see any issues, so, like, okay, the end. So…
**Juraci Paixão Kröhling** 49:24 Yeah, I had strange, auto-unplugged feelings from that… from that meeting, because, I mean, a lot of people with opinions, but then nobody actually working on those things, committed to doing things after the meetings, like… it was a nice time to talk to people, and nothing more than that.
**Severin Neumann** 49:42 Yeah, but… I mean, I did not attend that one, but, like, I also heard some maintainers saying, like, hey, was there no hotel-only time? And I had the feeling, like, from last Maintainer Summit, just sitting in a room with people and, like, seeing them face-to-face very often.
simplifies future async communication, right? So having… I think having OTEL and Prometheus people sitting in one room is already helping a lot, right? That people say, like, oh, I now know this person, and… I know at least one instance where an hotel maintainer told me, like, hey, Prometheus people reached out to me and are interested in working with me, so I think that's how I see it. So, yeah, less about doing work and more about meeting people.
But yeah, we could maybe improve.
And I think that that may…
**Juraci Paixão Kröhling** 50:44 Rongelo.
**Severin Neumann** 50:44 other thing, like… I think having more time for people from the community.
To meet and spend time with each other.
I think that that's also something I hear people saying, like, hey.
I said I missed the Sikh meetings, because, like, they were not easy to find, like, under those tables, but I said, like, oh, I wanted to talk with those people, but it was not enough time, or something like that. So yeah, if we can optimize for that in the future, I think that would also be great.
**Juraci Paixão Kröhling** 51:20 And I have an impression that I saw fewer boots, with, with OpenTelemetry native thing, like messaging.
So I feel like we are getting down to Earth.
**Austin Parker** 51:33 AI.
**Juraci Paixão Kröhling** 51:35 Yeah, it's.
**Austin Parker** 51:36 Everyone that was Hotel Native last year is now talking about how they're… the platform for your Agentic AI… Your open claws.
**Severin Neumann** 51:46 But there were a lot less AI SRE of vendors, right? That was at least, like, compared to North America. I'm not sure if it's just, like, those companies not showing up in Europe, but, like.
accounted, like, A lot less.
**Morgan McLean** 52:01 Or it could be.
**Juraci Paixão Kröhling** 52:01 So there was a third con happening.
**Morgan McLean** 52:03 real good.
**Austin Parker** 52:04 That's 3 calm as well.
**Juraci Paixão Kröhling** 52:05 No, I was gonna say that.
**Severin Neumann** 52:06 Yeah, okay, yeah.
**Juraci Paixão Kröhling** 52:07 So…
**Austin Parker** 52:09 I think there were, I mean, there were, like, there were some big ones that were, like… there were some companies that were definitely, like, leading with the AI SRE… Stuff.
**Severin Neumann** 52:19 There were some, but left, but it was just… yeah.
**Austin Parker** 52:24 Yeah.
**Juraci Paixão Kröhling** 52:34 But, Morgan, you had a comment or a question?
**Morgan McLean** 52:36 It was also just… there's a lot of the observability companies themselves that are offering AI SRE products.
But I do know that, like, Resolve AI, like, Spiros, I know the founder there quite well, and I don't know his rationale, but, like, they used to come to KubeCon, and now they don't. I don't… it wasn't out of grumpiness or something, but I just… I imagine he just, for whatever reason, didn't think it was as valuable as it had been in the… pass. I don't know his rationale, but I know they're not coming anymore.
**Juraci Paixão Kröhling** 53:10 So kubecton, I think, is tricky to get right.
**Morgan McLean** 53:13 Yep.
**Juraci Paixão Kröhling** 53:14 It is… like, the audience is not… like, it is not a sales event.
Right, so if you treat KubeCon as a sales event, then… then it's just wrong. You're gonna be disappointed.
**Morgan McLean** 53:25 And I think they also don't have an open source angle, like, his previous company, which was then acquired by Splunk, did, through OpenTelemetry.
**Austin Parker** 53:33 Yeah…
**Morgan McLean** 53:34 Right? Like, it…
**Austin Parker** 53:34 I think…
**Morgan McLean** 53:35 think they do anymore, and so that means, like, there isn't an easy way to sort of expand your presence there.
**Austin Parker** 53:44 Yeah, no, I think it's, it's… QCOTU also, it just says, is… Weird vendor mix.
**Juraci Paixão Kröhling** 54:03 Cool.
Yeah, so to answer your original question, Morgan, it was great. Busy, not easy.
**Morgan McLean** 54:12 Awesome.
**Juraci Paixão Kröhling** 54:13 And we should do more in Salt Lake City.
**Morgan McLean** 54:17 I'm excited.
**Juraci Paixão Kröhling** 54:19 And then, Barcelona, and the year after, is then here at home, Berlin. So, I don't know if you got the message yet.
**Morgan McLean** 54:26 I did not.
That's excellent.
**Austin Parker** 54:27 Yeah, Berlin would be fun.
**Juraci Paixão Kröhling** 54:28 versatile, yeah.
Trill.
Where's gonna be in the U.S. after…
**Marylia Gutierrez** 54:35 Because anyone, Japan?
No? No one going to Cupundra?
**Morgan McLean** 54:39 We usually send, like, one or two… usually, like, one person, maybe two, to Japan and, And I think we might be sending a person to India this year.
**Juraci Paixão Kröhling** 54:55 Cool.
Alright, folks?
**Morgan McLean** 55:05 Sounds like we might be able to wrap up 5 minutes early.
**Juraci Paixão Kröhling** 55:08 Yeah.
**Austin Parker** 55:09 Alright.
**Morgan McLean** 55:10 Alright, welcome back, everyone.
**Austin Parker** 55:11 Later on.
**Juraci Paixão Kröhling** 55:13 I'm excited.
**Trask Stalnaker** 55:13 Yay!
**Severin Neumann** 55:14 bye.
