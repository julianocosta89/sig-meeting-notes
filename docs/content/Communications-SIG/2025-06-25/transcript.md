SIG: Communications SIG
Date: 2025-06-25
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**TH Tiffany Hrabusa** 02:19 Kayla.
**Kayla Reopelle** 02:27 Hi, Tiffany, how's it going.
**TH Tiffany Hrabusa** 02:29 How are you?
**Kayla Reopelle** 02:31 I'm doing all right. How are you.
**TH Tiffany Hrabusa** 02:33 Good good is in the all day. Technical and governance committee meetings. I guess they're doing them all day today. And Patrice is out. I don't know if Fabricio is joining us or not. So it might just be the 2 of us.
**Kayla Reopelle** 02:52 Okay, I hopped on. Yeah, I I didn't realize there was that governance meeting today. I hopped on to check in about the getting started and reference application. I missed the the meeting last time around, but I'm curious where it's at for Ruby at the moment. I mean, I'm sorry where it's at, so that I could implement it for Ruby.
**TH Tiffany Hrabusa** 03:13 Okay.
I don't have a good status update on that. Hi, Philip!
The last I saw. Let me just take a look really quick.
**Kayla Reopelle** 04:11 I think. Yeah. The last I heard was that pull request was still open.
**TH Tiffany Hrabusa** 04:16 That's what I just found. Yeah, the pull pull request is still open.
But it looks like Severin is working on it, he commented yesterday, saying that he's going to rewrite something.
I I don't know what the next step is after that.
so I can make a note.
and I'm sure that he'll follow up.
**Kayla Reopelle** 04:44 Okay.
**TH Tiffany Hrabusa** 04:44 One second.
**Kayla Reopelle** 04:46 That would be great.
**TH Tiffany Hrabusa** 04:47 Hi, Lisa!
I can't hear you.
Yep.
**Lisa Jung** 05:03 Can you hear me now?
**TH Tiffany Hrabusa** 05:05 Yes, I can hear you now.
I was just telling Kayla there's a technical committee and governance committee all day meeting today. So Severn is attending that, and Patrice is out
for a couple of weeks. So we're
a bit of a smaller crew today. I don't have anything for the agenda. So if you have anything that you want to talk about, feel free to jump in.
**Lisa Jung** 05:39 Not this week. No.
**TH Tiffany Hrabusa** 05:41 Okay.
Okay. Philip, did you have anything?
**Phillip** 05:49 More just like a a lighter thing. So you know how
shit was it last week or the week before? I don't anyways within 2 weeks ago. We merged in the
the proposed changes to add python logs. Even though it's still technically under development. Just kind of under the assumption that like well, it's probably more helpful to like. Tell people how to do it, because it's probably like
the code is like close enough to like what it's going to be when it's actually shipped. And the python folks seemed okay with that which I think is great. I'm now wondering about the other the other Sigs. And if there's some sort of like upfront communication that we could do would be like, Hey, like from the website perspective.
You know, we generally think like
the lack of how to do this. This concept, even if it might be subject to some change, is, is worse than you know, getting people to learn how to do it one way, and then, like one Api changes, you know, a couple of months later, or something like that.
**TH Tiffany Hrabusa** 06:52 Oh, okay, so like the inertia of things might change. So we don't write anything but having nothing is really bad, too.
**Phillip** 06:59 Yeah, yeah, like, I, I would rather have stuff that like, you know, there's a disclaimer saying it might change a little bit. But you can use it, and it'll work for you. Instead of somebody getting the impression that like, oh, this language doesn't support this thing at all, and that's what I need right now. And it's like, no, it actually does. It's just, you know, you might have to change things like 6 months from now, when stuff changes, whereas I think, like
I don't know, I feel like the general way that maintainers tend to work is they're like, Okay, well, only when it's stable. Should we really document it? Because then, you know, we know that we're not gonna go after gonna have to go back and change stuff for people, and they're not gonna have to deal with breaking changes. But like.
I feel like a lot of people are okay with dealing with a lot of breaking changes.
**TH Tiffany Hrabusa** 07:42 Yeah.
**Phillip** 07:42 So
**TH Tiffany Hrabusa** 07:43 Hotel, right.
**Phillip** 07:44 Yeah. Yeah. And if you're gonna sit around waiting for Ga, you're gonna be waiting for a long time, because that's kind of how things work around here. We've missed every deadline we set.
so I I don't know. Maybe there's some kind of like communication to the other Maintainers that we could do where we could say, Hey, like.
you know, still sort of like your call as language maintainers. But if you feel like it's usable, and it works.
We will happily accept
docs, changes or something. I don't know. They're like, I'd like to propose that. And you know, we kinda
prance around the different Maintainer Sigs, and tell them that.
**TH Tiffany Hrabusa** 08:21 Okay.
Kayla, I know that you're in one of the language. Sigs. Do you have any thoughts about that?
**Kayla Reopelle** 08:26 Yeah, I think that would be excellent. I it's kind of weird with the way that the statuses are set up right now that it's kind of sorry. I don't know if you can hear my dog drinking water right next to me. It's kind of in development and then stable. It doesn't feel like there's a whole lot of room for changes. And I I think there's a Pr proposed somewhere to have more levels. But
we get a lot of confusion about how usable something is. So I feel like having more docs about. The stuff that we are like trying to march towards stability might encourage more users in that kind of funny. In between time.
**TH Tiffany Hrabusa** 09:04 Okay.
**Lisa Jung** 09:05 I'm just curious. Is there a slack channel just dedicated for all the maintainers within the space
there is okay.
**Kayla Reopelle** 09:14 Yeah, and it's, it's.
**TH Tiffany Hrabusa** 09:15 It's an open channel.
Yeah, it's just called hotel Maintainers.
**Lisa Jung** 09:20 Sweet. Okay, thank you.
**Kayla Reopelle** 09:22 And then other than that there. The
Tc. Meeting or the the spec meeting on Tuesday mornings is also the Maintainers meeting now. So if you go to that meeting you should be able to hit the full group.
**Lisa Jung** 09:35 Cool, cool.
**Kayla Reopelle** 09:44 But, Philip, you're saying python just merged in a Pr recently about like logs, adding logs, documentation.
**Phillip** 09:51 Yeah, yeah, the the the context was, they're prepping a release candidate. And so they're like, Oh, great, yeah, we should have docs that show how to use it, and then let's let's hold off until the release candidate is out, and then I'm like.
well, it seems like the code is the same. So why don't we just merge it.
**Kayla Reopelle** 10:06 Right now.
**Phillip** 10:07 And
whatever disclaimer we need. And that got me thinking like, okay, you know, like what other languages out there are there where you know.
Yeah, you might as an end user. A couple of months from now you might have to put up with a breaking change. But, like realistically, if you adopt whatever the package is right now, like, it's going to work.
**Kayla Reopelle** 10:24 Yeah. Yep, yep, Ruby's in that boat for metrics and logs.
We're still far, I think, a ways off from a release candidate, but that's mostly due to capacity for logs and then metrics. We do have more features. We need to implement.
**Phillip** 10:37 Okay.
**TH Tiffany Hrabusa** 10:39 I just linked the the python logs. Pr, if anyone is curious about the discussion that happened about whether to release it or not. So
And I'm going to add it to the notes as well. Hi, Sophia, welcome.
**Sophia Solomon** 10:56 Hi, everyone. I'm a new developer advocate at Elastic, and I have kind of my specialty in like open telemetry and
observability in general. So I just wanted to join to kind of get in the in the wave and say hello to everyone.
**TH Tiffany Hrabusa** 11:17 Absolutely welcome. It's really nice to have you.
I'm just finishing up some note taking. So if anybody has anything else feel free to speak up.
**Phillip** 11:36 yeah, my! My only thing is Tiffany, for for that one like I can take the ball on that to
**TH Tiffany Hrabusa** 11:42 Okay.
**Phillip** 11:43 Posting the Maintainer, Sig and
I. Well, I'll probably do like a little bit of an audit of each of the major languages, and and be like. Is is this like a relevant thing to bring up to them or not? And then
and say, Hey, this is what we want, and let's figure out how we get there. Like, you know, I'm certainly not above authoring content myself. But you know, if one of the one of the maintainers or approvers. And one of those Sigs is like, Hey, I'd actually love to do this like hell. Yeah, great.
**Kayla Reopelle** 12:07 Yeah, I feel like for me. I'd be happy to do the writing. But I just need to know, like, if there's examples and also understanding where in the doc site there's just kind of like empty spaces right now, because we don't have those things implemented like both of those things would be very helpful to get me started.
**Phillip** 12:26 Okay, yeah. I think we can definitely define
sort of like where we would expect those docs to slot in and and it's also definitely not like, you know, you can only do it. A 100% or or nothing type deal like
like, there's a canonical example in the getting started. But if like, for some reason, it's really awkward to wire it up, you know, for that one like it's fine. So.
**TH Tiffany Hrabusa** 12:55 I know also that
The communications thing in general has been trying to
break up workloads in more organized ways. And one of the ways that we have started doing that is,
there's a list of basically the different parts of the website. And I know that Fabrizio is actually one of the people who volunteered to take on docs for the language sigs, so he may also, if he's
if he's in the docs, he may be able to help identify the gaps that exist.
so that's another resource that you could tap into.
Okay.
I'm supposed to be starting the refactoring of the collector documentation.
I haven't gotten very far with that yet. The fire drill last week with
the whole Cmcf. Slack thing.
I we did manage to actually
save the entire hotel dash collector channel like going back, I think, 4 years now. So now I have that information, and it will never be lost. But I was going to use that to kind of
mine for the top
complaints that we get about the documentation so that we can figure out where to start there.
If anybody is interested in helping with this project, I'm open to taking volunteers to help
But yeah, that's I have nothing really useful to say at this point. It's I haven't made any progress.
**Lisa Jung** 15:08 So are we officially switching over to like discord, or like other messaging platforms now, or like what's going on.
**TH Tiffany Hrabusa** 15:16 The Cncf worked with salesforce, and I guess they've reversed the position so.
**Lisa Jung** 15:23 Oh!
**TH Tiffany Hrabusa** 15:24 We still have a an enterprise level, slack.
**Lisa Jung** 15:29 Sweet. Okay.
**TH Tiffany Hrabusa** 15:30 How long that's going to last.
**Lisa Jung** 15:32 Yeah.
**TH Tiffany Hrabusa** 15:33 The Cncf.
Like leadership hasn't said that. They know for sure that it's indefinite, so we'll just have to see
what they communicate about that in the future. But yeah, for now nothing changes.
**Lisa Jung** 15:47 So it's okay to refer to the hotel slack channels as like one of the resources.
**TH Tiffany Hrabusa** 15:57 Yes, yeah, I think, for now it's safe to continue doing that.
**Lisa Jung** 16:01 Thank you.
**TH Tiffany Hrabusa** 16:33 anything else. Anybody have, anything else.
**Kayla Reopelle** 16:37 I don't know if this is the right sig for this, but I am presenting at a conference soon, and I was wondering if there's any like
an easy place to get hotel stickers or other things to hand out. Related to hotel things.
Maybe that's an end user sync question. I'm not really sure.
**Phillip** 16:58 And so Austin Parker tends to print a ton of stickers and.
**Kayla Reopelle** 17:03 Oops!
**Phillip** 17:04 Some sort of where he's at a lot of the hotel events. But, you might be able to ping him, and like he.
he has access to a lot of like the different designs. And so
I don't know if you know, if it would be like, you know, he ships them, or something like that. But, like he, he's traditionally been the one who, like comes with just like a giant bag of.
**Kayla Reopelle** 17:22 Cool. Sounds good. I'll check in with him. Yeah, cause it's a it's a ruby conference that I'm talking about hotel at. So not not other hotel people there probably.
**Sophia Solomon** 17:36 Oh, yeah, I also had like, kind of an adjacent question, is, anyone does anyone know what's going on with the developer experience that happens kind of in like 45 min. I've been joining for the past like 3 weeks, and no one's been joining, but if no one knows, then cool.
**TH Tiffany Hrabusa** 17:54 Oh, I didn't realize
No, I don't have any information about that. I'm trying to think.
**Sophia Solomon** 18:02 Cool.
**Kayla Reopelle** 18:03 The only thing.
**TH Tiffany Hrabusa** 18:04 There's.
**Kayla Reopelle** 18:06 I think, like Damien
Matthew, I'm I'm probably pronouncing his name wrong. He's based in the EU, and I don't know if there's also like an EU time slot for that meeting, but he's been really active in the past, and I wonder if dming him might be a good way to check in.
**Sophia Solomon** 18:24 Yeah, okay.
I think he might also be at elastic, isn't he?
**Kayla Reopelle** 18:28 Oh!
**TH Tiffany Hrabusa** 18:30 Think.
**Kayla Reopelle** 18:31 Do you.
**TH Tiffany Hrabusa** 18:32 I might be wrong about that, but.
**Sophia Solomon** 18:34 Oh, I think Damian Math. Yes, immediately pops up. Okay, yeah. Let me message him.
**Kayla Reopelle** 18:40 Thank you.
**Phillip** 19:04 Not an official topic item, I guess. But now that
Google released the Gemini cli and Cloud code exists, a lot of people use them. Not a lot of people are aware of the fact that these are default instrumented with hotel and operations that they do are traced, which is really cool. You can actually just point your cloud code running instance. And I guess now also your your Gemini cli instance to an observability back end and be like, Hey, cool. This is like what happened when I tried to do stuff
and
I don't know. Maybe there's there's there's something to sort of say about that about how like for a lot of the the AI Dev tool stuff like they're just like automatically picking open telemetry and saying, Yep, we gotta emit data, because that's how you understand what the heck happened and hotel. Is this the standard for that? And thus there you go.
I think that there's like some cool storytelling to do around that potentially Austin has done a little bit of that himself as well, but
yeah, there might be something there. Just a thought.
**TH Tiffany Hrabusa** 20:21 Okay, that would be, I think, a good fit for
Everyone's been talking about bringing on someone who works in his company who's in marketing
and so bringing in someone who could do more of these like
like color pieces, I guess, like, you know, bringing to light different ways. That hotel is being used. Different things that are going on in the Sigs like that kind of stuff. So
I'll we'll ping Severn about that.
**Phillip** 21:03 Yeah, I I think, like in particular, this one, I I find pretty exciting, just because so many developers have picked it up and and are using it. And it's like, Wow, yeah, this thing is like.
they just chose hotel for really good reasons. And it like, Claude. Sorry anthropic. They they have like docs, sort of describing how you can wire up the the telemetry and stuff which is also pretty cool. But like that also, there's been like this like long standing
thing of like, how do we? How do we bring hotel a little bit closer to developers and make it feel like more relevant to them. Because, like the sre category of people like.
they're like, well, yeah, duh, you need telemetry to like, understand what's going on in your systems, of course, but like a lot of developers out there in the world are kind of like they live in a bit more of a silo where they're like, well, why do we even need this but and traditionally, one of the hooks to get them was like you instrument your Ci process, and then they're like, Oh, wow! Our builds do this! Oh, my God, wow! This is so. We we found out. But this kind of could have a similar sort of sort of impact potentially so.
**TH Tiffany Hrabusa** 22:16 Okay, I think that's a great idea.
The duties from one T, and I guess, too. But
yeah, I know Severn really wants to do more of this, and I think he's right that that is
Right now. Our.
our outreach is very reactionary. Whenever someone writes a blog post and comes to us. We advertise the blog post.
We don't do a lot of proactive social media to like from the communications perspective. So I think it would be good to start looking for opportunities just like that where we can
be more vocal about the fun stuff that's going on with Otal.
Okay, I thought it was gonna just be me today. So this is actually exciting. There were a lot of us here.
Does anyone have anything else.
Okay, well, we can get 40 min back in our day.
**Phillip** 23:33 You know it.
**Sophia Solomon** 23:34 Okay? Bye.
**Lisa Jung** 23:36 Thanks. Everyone.
