SIG: Browser SIG
Date: 2025-07-31
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:32 Hello!
**Martin Kuba** 00:37 Morning.
**Dan Gomez Blanco** 01:17 Hello!
**Martin Kuba** 03:03 I think we're just waiting for Ted.
and he might. He might be still in the other sig in entity. Sig.
**Jared Freeze (embrace)** 04:00 But thanks before this.
**Martin Kuba** 04:05 Sorry. Sorry Jared.
**Jared Freeze (embrace)** 04:07 Oh, you! You said he would. He might have been in another one. I was just curious what it was.
**Martin Kuba** 04:12 The entity sig?
Well, I guess we can get we can get started like, actually, the 1st 2 topics are from me.
yeah. So what I wanted to talk about is couple of things. We have a few semantic conventions. Prs, that we want to finalize. I think I shared them in previous meetings.
and the one that I've been looking at is the page view one.
And but since, since, like the the semantic conventions were discussed a long time ago with different group of people. I wanted to just get a consensus from this group. That that's the direction that we want to continue in, and whether we should push this Pr through? Or can I revisit the discussion?
Let me just share my screen. Really quick.
so so basically, like, just just a quick summary, we we proposed, we have 2 prs that are that relates to the page view 1, 1, we actually called Page View, and it's this pr and the intent, the intent of of this of this event. So this will be an event would be to capture mostly the counts.
So like how many you know how many users are are loading this page?
And the the other so that it wouldn't actually wait until any timing data is is available. It would be captured as soon as possible as soon as as soon as the instrumentation loads and the other events that we would capture for timing data would be specifically the navigation timing event. So when that is available where all the navigation timing data is available, we would capture that as as an event, separate event.
And so I want to talk specifically about this page view one.
So one thing that I wanted to a couple of things. So I just want to. Want to get a consensus that like this makes sense for us. Like to have these 2 events.
And then the other thing that I wanted to get everyone's feedback on is whether the page view event should be used only for, like the hard navigation for page loads.
or if it should also be used for soft navigations, like when the URL changes in the browser.
like, you know, single spot, single page applications making a route change currently the way it's written and the way we discussed it in the past is to do both. So if you look at the Pr there is a type type attribute here which would be either the type of navigation which would be either, or is it discussed.
it would be either route change or like page load.
Yeah, initial page load is 0 and the route change would be would be type type one.
But I'm not. I'm not actually convinced that it's it makes sense. And I wanted to get everyone's feedback on this
**scheler** 07:55 What is your reason why it?
You think it doesn't make sense.
**Martin Kuba** 08:02 So I think I think one is that the self navigation is not necessarily well defined. It's, you know, there is no like spec for it, I mean, like the URL could change, but sometimes it may represent a page navigation. Sometimes it could be just like changing the fragment or changing. You know the part that doesn't actually represent actual change of view.
I think there is a there is a there is a proposal that's that's in progress that talks about soft navigation. And there's like the definite definition would be like an event happens. URL changes, and also the view changes.
So I think it would be tricky like to to for us to figure out like what actually does represent a self navigation right now.
The other reason is that they're they're like, very different. 2 different kind of thing. Events like 1 1 is. The hard navigation like is loads all the resources it initializes everything, whereas the self navigation is, is is is a different like. It seems like a different type of event. But.
**Ram Thiru (MSFT)** 09:17 Yeah, great points, Martin. I can talk from experience. You know, we've dealt with this. Gosh, you know, 10 years ago. Something like that. When when you know I don't know if it's that's it's that long but since past became really popular, and everything it I think it comes down to. What really do we want to track with these events and stuff? Right? So what's the back end trying to do with this.
if it's only performance based, you know. Probably Page navigations is something that we can simply hard navigations, something that you look at. But most most of the times. It's used for business metrics, for business metrics. If spas only tracked page views and hard, hard navigations. That's a useless metric.
They're gonna see, you know. They probably literally had like a million views, and they can only see a thousand of them in the back end, and they'll they'll freak out the the people that consume the data will freak out. So that's the thing that we have to 1st come to in a conclusion. On what exactly are we going to address with these events? If it is not like truly what bits my servers serving, or whatever it is like hard navigation and stuff? I don't believe that's a useful metric anymore, at least for browsers.
If it is logical page views, then combining them together into this page view thing is that I think that's kind of what we arrived at. We went through several iterations in Microsoft multiple sdks.
We ended up with that. So soft navigation is the thing that we want to definitely track it's not going to be the best like you said. You know, great arguments made right. It's not going to be perfect. It's not well defined. We don't know when to do. Maybe the over count, or whatever how we've solved it in the past is if a consumer is somebody who's going to use our SDK.
Is going to decide. Oh, my God, I'm seeing way too many of these like in a chatty you know, logical navigations, or whatever it is, if you will, they can turn off that auto capture of the soft navigation. But then we give them a Api to go call it if they, if they feel like enough of the content, has changed. They trigger a page. View.
So that's a that's an option that we've done, and that's worked really, really well with all of our consumers.
**Dan Gomez Blanco** 11:24 I guess that that also means that any timings need to be, I guess, is the current approach right? You've got page navigation timing as a separate event, because anything that you put in there in terms of performance would be completely different for page view, for a hard navigation and a soft navigation navigation, right?
So it would make sense to.
Yeah, I think it makes sense to me as well.
**Martin Kuba** 11:54 Okay, some sounds. So I think, we can just just move. Move forward with the with the Prsas, unless somebody has different opinion.
**Benoît Zugmeyer** 12:07 Just a small question about the navigation events like.
why does it need to be different from the the page view?
Can cannot. Can the the page. You include all the information already to navigation.
**Dan Gomez Blanco** 12:25 The I mean the timings, and then the.
**Benoît Zugmeyer** 12:28 Yeah.
**Martin Kuba** 12:29 Navigation timing, you know. I think I think the reason is that just the reliability of the of the getting that event sometimes, like the page load may not, you know, takes a long time, and may not even finish until when you know the user could leave the page even before that event fires.
You know the page navigation timing like you can.
I think there's there's an observer so you can. You can get notified when all the timing information is available, but you can also like request it on demand. So when the page is unloading and you want to capture whatever we have up to that point like you could just like capture the timing data at that point.
But I think the main reason, in my opinion, is that it's like you want to like. If you want to have reliable accounts of users like you don't want to wait until you know some event fires up which may never fire.
**Benoît Zugmeyer** 13:25 Right.
**Dan Gomez Blanco** 13:26 That sounds great.
**Benoît Zugmeyer** 13:28 Just a quick follow up question.
I'm sorry if it's a naive question. But is there any concept of event updates like to update the data from in a in an event.
**Martin Kuba** 13:48 You mean before it's collected before it's captured.
**Benoît Zugmeyer** 13:54 no, after it's like, can can we send a a new version of an event like replacing the other one? The the previous one like, for example, for page views, we would send a a small page event right? When we initialize the SDK.
And then, when we have the navigation information we would just like updated.
Is it possible?
I don't know.
**Ram Thiru (MSFT)** 14:22 The yeah don't don't know. Even the updates are a thing in huge telemetry systems. It's gonna be really, really hard. I think that's why, I think they combine these events in the back end. You have a way to, you know. Combine your page navigation page views with the navigation timings, you combine them and essentially create a holistic view instead of an update. It's it's like a soft update, so to speak. You have to do it in the back end. I've never heard of telemetry systems being updatable.
**Benoît Zugmeyer** 14:51 That makes sense. Thanks.
**Martin Kuba** 15:01 Okay. So if there are no more comments on this, then I would ask if you can, please look at these 2 Prs, the semantic conventions. Prs.
if you have any additional comments, please put them on the Prs you know, it'd be good to to get those. Get those finished.
yeah, as far as as far as semantic conventions.
Okay? And the other topic that I have is I've been working, you know, for a long time. Now on on the session manager there is a there's a Pr that's that's been open for for a long time. Now that actually has a prototype implementation of of the session manager.
And it's you can let me see this.
Okay.
yeah, there is an issue in Contrib where this was discussed before the implementation. And there is there's a diagram of, like all the different components that go into this prototype and how it was designed.
what I. What, I wonder is, since again, since this was worked on a while ago, and this is new to this group.
would it? And there are. Maybe you might have some questions, so would it make sense to kind of step back and have this discussion from the beginning? Or do you just want to take a look at this proposal, the the prototype instrumentations, and discuss on on there.
and I can. I can walk through it if that makes sense. If anyone would prefer.
**Ted Young** 16:57 This. This just contains the session manager. Right like we don't.
**Martin Kuba** 17:00 Session, manager.
**Ted Young** 17:01 Entity providers and stuff like that.
**Martin Kuba** 17:03 That's right.
**Ted Young** 17:04 You know, given given that this is kind of this is all prototyping stuff, and you know I would be in favor of like, you know, like going ahead and merging it so that we can play with it, and then just like continuing to to iterate on it right like we're not anywhere close to even a beta yet. So.
**Martin Kuba** 17:27 Sounds good. So so with that, said, I think there were some recent comments, I think, from Benoit and from you. So I made those changes. So please please take a look at them.
and I think if those, if there are no more comments, maybe we can, we can drives this through being merged.
**Ted Young** 17:49 Bye.
**Martin Kuba** 17:51 Cool.
I'll stop sharing my screen.
**Ted Young** 17:57 Oh, can share my screen.
I got the rest of the topics. So one of them just a question kind of like, prompted by what we were just talking about. We've discussed needing maybe some some kind of like RAM. You were just walking through like like what I thought was like a a good example of like, how how you guys are planning to use the data and how how we intend to use this data, you know, influences what data we're collecting.
I'm just wondering what what is the best way to kind of capture that that seems like a document we would want to create. To just be like, this is kind of our our data model. And this is either working back from like our intended goals of like this is what kind of you know, observability we're trying to do in this 1st version.
Something like that, you know.
**Ram Thiru (MSFT)** 19:00 Yeah, great question. I think so funnily enough. 2 years ago something like that, when this group, which was not fully approved, came together, Martin Santosh myself. Nev. And you know a bunch of others got together people from Honeycomb, Purvi and others got together. We did the exact same thing. We went through a pretty laborious exercise.
I was all of the Llm's. AI. Was available back then. It was pretty manual, but we did go through that we captured it. It's somewhere I I lost track of where it is at. Maybe Santosh and Martin can fish it out, or something like that.
I don't. I'm not saying we should start with that. But that work was done just recently, like about 2 years ago, or something like that.
**Ted Young** 19:39 Yeah.
**Ram Thiru (MSFT)** 19:39 If it is anything different, you know. We can definitely talk about it. If it's the same thing, we should definitely see if we can glean some info from that.
And then, of course, you know, new blood and everything here. We'd like to hear from everybody else, too. So yep, Santosen.
**scheler** 19:56 Yeah.
**Ram Thiru (MSFT)** 19:57 Yeah, did you guys hear what Ted was saying? Is to be different than what we did a couple of years ago?
**scheler** 20:06 I I in personally. I I feel one of the goals should be to finish the transition to the event based telemetry because that that was one of the critical items that that's being taken up, you know. Secondly, we have always had concerns with the performance and payload sizes. But that's more of an optimization. I I would like to look at it as a phase 2 so as a 1st goal like we and and many of the vendors you know, we have already been using. The, you know what is currently what instrumentations are currently there. But you know there is a there is a lot of confusion on our side at least that a lot lot of these are represented as pans, whereas, you know, they don't.
Necessarily, you know, span is not necessarily the right data model. So we do want to transition. But we want to transition at a point where you know everything is complete, you know not one or 2 instrumentations being there. So for me, a best way to adopt 2.2 instrumentations would be when the event based.
Instrumentations are complete.
**Ted Young** 21:26 Okay, I I think it would be helpful to one. I would love to see the work that you all did in the past. I mean looking through the work on all of these different browser events, Martin published the last last week, was like super helpful to me. So if anyone can can find that.
**Martin Kuba** 21:44 That work I would love to.
**Ted Young** 21:47 Love to see it.
And maybe just just something. I know you're getting into the details Santosh around like spans versus events and things like that. I almost feel like, maybe, like a just starting from like the end goal of like we're trying to like. Do these observability tasks in the browser, you know some something like that, just to guide some of the questions RAM was was asking earlier about like, Why do we capture these attributes, or why do we capture it as a span or an event? We, it seems like we would need to know the goal before we could.
We could answer all of those questions right?
**Martin Kuba** 22:30 So I would say just a couple of things like, last last week I did share the documents that we worked on, you know, a couple of years ago, as RAM mentioned.
there was a there was a word document where we listed all the all the different data that different vendors are capturing, and and then the spreadsheet. That's where we decided on on the convention that we decided on, and I also listed the the cement conventions Prs, that we have open right now.
There's also a data model document that I that I shared. I think couple a couple of weeks ago.
Maybe maybe we can, you know, add some use cases to that document or discuss things there.
**Ted Young** 23:12 There was some good data modeling buried in like the the spreadsheet and stuff like that. Okay, so maybe that those are the docs.
Yeah, he, you were talking about.
**Martin Kuba** 23:21 Yeah.
**Ted Young** 23:22 Okay.
**scheler** 23:27 That would be an intermediate state. Right? I think the data modeling exercise is a must, you know, for a good quality output. But at the end. Our our goal is to finish the implementation as well. So that then we can call it like, okay, there is some something we delivered.
**Ted Young** 23:48 it's you know, we can always add more things later, we can add more attributes later. But yeah, like you're saying, like is, do we gonna represent this as an event or span, you know, like, those are like like pretty big questions that we got to answer answer quickly.
I. So I have. Unfortunately, I have a have a hard stop for myself. at the end of the hour just to to get through the conversation last week. With backlog management. It seemed like we wanted to change the order of attack.
And I kind of agreed with this to Hector, do you mind? Muting sounds like you're yeah.
It looks like What we'd like to do is like, just focus on these semantic conventions and and modeling the and getting some instrumentation out there 1st right and then go back in and look at revamping our Api and like optimizing things and things like that that seemed that's the almost the opposite order of what we initially put in the Doc. But I think it's better. So I went into our project roadmap.
and I cleaned it up.
Hello.
sadness!
Well, poor Timing Github.
**Daniel Dyla (Dynatrace)** 25:27 I've been having on and off problems all morning.
**Ted Young** 25:31 Only it was observable what it was doing.
Well, this is taking too long. I'm gonna switch to gitlab, I guess.
Well, I wasn't able to get in there. We're gonna run out of time. Let's.
**Martin Kuba** 25:51 I can. I can share my screen if you want. I have.
**Ted Young** 25:54 Got it loaded up all right. Here it is great.
So I cleaned up a couple of things one for this.
This view I got some feedback, having everything on the kind of like roadmap view wasn't helpful. So I just limited this to to just the high level projects.
And it seems like what we'd like to say. Going forwards is like, so right now, we're going to be working on semantic conventions, sessions and entities and instrumentation.
And then in the future we'll be working on Api test harness and prototyping.
Going to the task picker.
I got rid of everything that we were speculating about in the future, and just boiled it down to the the active projects we were talking about, semantic conventions, sessions, and entities and instrumentation, and then I went in and added.
every some version of every event that I saw in your doc that you had published from last time. Some of these are links to, you know, existing Prs or issues. And the rest, I just added, as as draft this to me, feels a little bit more like sane and contained.
I'm curious what other people think about this? Does this feel like the right direction? Because, if so, the next step would just be to start assigning these different semantic conventions to people that no one's currently working on to to start hacking away at.
How does that sound to people.
**Jared Freeze (embrace)** 27:48 Sounds good to me. I did have one note which is like the staleness timer seems really short, so like I often open stuff, and I'm like, Oh, why are they done with this? And then at the bottom, it just says, not stale, and then immediately closed again.
I just that's a little confusing. So.
**Ted Young** 28:07 Okay.
yes, yes, we're pretty aggressive about that these days, and I need to double check. If there's a label we can apply to kind of shoo the staleness away from stuff that's I I'm a little nervous about. I I've been actually reluctant to turn these things into issues for that reason, because we don't. We try to like keep the backlog like clean and small, I mean, and it's still big and like having, like like huge piles of like speculative issues out there doesn't doesn't feel great. That's partially why we have an aggressive staleness.
timer. But it does leave us in a situation where, if we're not gonna use, you know, a pile of like.
you know, issues we aren't touching in the backlog to manage this. How do we do it? Maybe we just manage it through here.
but if people are interested you can come in for any of these that are draft, and you can assign yourself to them if you're interested in working on this. And, Carly, I think this one was yours.
This was closed, but you could, I think, just reopen it.
**Karlie L** 29:27 Yeah, sure.
**Ted Young** 29:29 Great.
**Karlie L** 29:30 Yep, thank you.
**Ted Young** 29:31 Okay. So I I have to leave. I have a hard stop. But feels feels like we're we're getting our feet under us. So I'm excited.
Cheers.
**Dan Gomez Blanco** 29:50 Alright, I think that's it for today. See ya.
**Hector Hernandez** 29:55 Thank you.
