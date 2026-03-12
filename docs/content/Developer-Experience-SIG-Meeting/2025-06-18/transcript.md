SIG: Developer Experience SIG Meeting
Date: 2025-06-18
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:15 Hello! Hello!
**Tristan Sloughter** 00:21 Yo.
**Juliano Costa | Datadog** 00:23 What up can you hear me?
**Tristan Sloughter** 00:28 Much? How's it going with you.
**Juliano Costa | Datadog** 00:31 Oh, good! All good. Yeah.
Back back to work, to normal work, so to say.
**Tristan Sloughter** 00:38 Okay. You were in the Us.
**Juliano Costa | Datadog** 00:40 Yeah, I was there for for dash last week. So, yeah, and the the month start the months before the event are like, yeah, total focus on the event. So.
**Tristan Sloughter** 00:54 Yeah.
**Juliano Costa | Datadog** 00:55 Now I can focus on hotel back again.
**Tristan Sloughter** 00:59 Nice, nice, good.
**Juliano Costa | Datadog** 01:04 How, how are things in Canada?
**Tristan Sloughter** 01:07 Pretty good, pretty good.
Couldn't finally feel settled, and through the lunchboxes, except for the things that will stay in boxes forever. So those are just in boxes in the basement till the next move, and they can just go.
**Juliano Costa | Datadog** 01:26 Awesome.
Well, yeah.
**Tristan Sloughter** 01:35 Oh, yeah, Steve's not coming, but
**Juliano Costa | Datadog** 01:37 Oh, okay.
**Tristan Sloughter** 01:39 Hey, man! How do you.
**Juliano Costa | Datadog** 01:40 The I don't check that chat.
There you go.
I wonder if we if we have something to to actually take a look.
**Tristan Sloughter** 02:25 Would you? Have you spoken to the person at Mastodon at all?
**Juliano Costa | Datadog** 02:33 Well, he just agreed. But I haven't I I didn't go back with to him with the proposal, because I think we need to still define what we want to.
The the structure of the.
**Tristan Sloughter** 02:52 Yeah, we kind of yeah, very broad strokes of what we want to cover.
But actually, the yeah, I've been trying to think about what it should actually look like. And you know, just and blinking the.
And I told the person the end user group.
You know the 2 sides of what we have Macedon and Atlassian, and they'll probably have somebody what they can do in the middle medium size, and then figure out who talk to them. But depend on time zone, probably the and I'll talk to Atlassian once we have decided on. You know what we're trying to tease out of them exactly.
We have discussion topics. But yeah, I don't know how we wanna structure this. And.
**Juliano Costa | Datadog** 04:03 You know.
**Tristan Sloughter** 04:04 Something that would be most useful to to readers to.
because it's not a tutorial. It's not just a an interview.
Oh, you know, like, oh, so you use a hotel, but it's supposed to have useful information of you. Had to use hotel interesting. Mix.
**Juliano Costa | Datadog** 04:32 I don't remember where it was.
but I think Cncf had had a blog, or somewhere where they had like architecture. Kind of, not samples. But I don't remember jeez. I need to to find a word to actually Google for it and try to page. But it was like a page where they had some reference for architecture, deployments, or choices, and they they were kind of presenting best practices on the industry and stuff. So maybe we could take take a look at that, but I need to find first.st
**Tristan Sloughter** 05:25 Okay, yeah, that sounds like a a match.
That'd be good. I wonder if the and put people at the end user group, too, if they just in general have any dots on this kind of post, because they might know something similar to that from oh related content.
not necessarily from open telemetry, but from other projects.
**Juliano Costa | Datadog** 05:53 Take a look if.
**Tristan Sloughter** 05:55 Okay.
**Juliano Costa | Datadog** 05:55 It's like architecture. Dot Cncf dot I/O.
**Tristan Sloughter** 06:00 Oh!
**Juliano Costa | Datadog** 06:01 So it's like, so they kind of spotlight a company, and then they tell the the company story.
I mean, it doesn't go much in details just pretty detailed.
**Tristan Sloughter** 06:27 I mean in the broad stroke. The you know, it's got diagrams and everything that would be awesome.
**Juliano Costa | Datadog** 06:33 Yeah.
So maybe we could try to do something like that.
**Tristan Sloughter** 06:39 Yeah.
**Juliano Costa | Datadog** 06:40 And and maybe Link, I don't. But no, I I would rather keep on Hotel dot I/O instead of publishing here.
Yeah, no, I think it makes more sense in the in the hotel blog and it would be more visible for the hotel community in the hotel, page other than here. But
**Tristan Sloughter** 07:10 You.
**Juliano Costa | Datadog** 07:13 Yeah. So we could, we could try to do something like this architecture diagram that they have.
So like to showcase how they, of course, focusing on the collectors, and where they where they added, where they added.
I don't know if we need to mention other projects.
Like right.
**Tristan Sloughter** 07:42 Yeah, it might be. Depend on how really, I mean stuff that it might be like a how they roll out deployments, or something could be related. So if they're using Argo, or something like adobe's post how that fits in to roll out configuration changes to, you know.
thousands of collectors, or something could be.
It could be related.
**Juliano Costa | Datadog** 08:15 Hmm!
Oh, the the one from from adobe is way more detailed than the.
**Tristan Sloughter** 08:28 Oh, really, yeah, that's the one.
**Juliano Costa | Datadog** 08:30 Yeah, yeah, no. I checked the the 1st one. And the the ones from Allianz audience. And it's like, really, yeah, it's much shorter yep with the one from adobe Springfield.
I like that. And I think eventually, if we get, let's say, 3 blog posts or so we could. I? I could try to discuss with the Docs team to have some like architecture section on the docs to kind of have like references to people to to take a look.
I think it would be a nice addition, or because the blog post is nice, but then it gets lost.
**Tristan Sloughter** 09:31 Right, exactly as it gets older.
**Juliano Costa | Datadog** 09:34 But I'm
**Tristan Sloughter** 09:35 I think.
**Juliano Costa | Datadog** 09:36 Need to to get.
Yeah, I think I think we need to get things out first, st and then we figure out where to put, and what to do with it, but.
**Tristan Sloughter** 09:45 Where to grow with it, yet.
Yeah, that'd be big. That seemed to be what people were asking for.
How do I actually structure these things in my environment?
The only read all these architecture posts.
Let's see list, or the week before.
I think we have pretty good discussion topics, maybe just need to write up a structure around those for the trying to think of trying to structure the conversation or the blog post would make more sense like structure, the blog post, and then we can base the conversations off of that, or just try to have conversations and see where they take us. And and I guess, trying to approach them separately from the interviews and say.
can you share this kind of stuff because of like a things we won't be able to good through an interview of like pieces of configuration and architecture diagram. So we should ask them for those things first, st and then an interview.
Go from there.
See what they can share. I assume mastodon's gonna be easier to get things shared out of. But the hopefully Atlassian will share plenty. Probably.
Yeah.
And yeah, I mean, we might just wanna do these interviews based on this our discussion topics and and then kind of trying to go from there. The I don't think we're gonna be able to really plan out that detail that fits both of the companies or all 3 of the companies. So.
Plan for each one, individually or together, and partially just free flow of.
We know we wanted what we want to discuss.
We don't need.
Questions or anything.
**Juliano Costa | Datadog** 12:54 Yeah, I I don't think we need the exact questions. You're right. But I I think we need kind of a structure. If you take a look at the at the this architecture page and compared adobe with audience, you see that it's pretty different. The blog posts like.
**Tristan Sloughter** 13:14 Yeah.
**Juliano Costa | Datadog** 13:14 Post itself, but I think they do share some common common ideas like the diagram, for instance.
Oh, my!
Think, that would be nice to have, you know.
like, yeah, you have one collector. Here's your app, whatever. And then one collector. Or here you have like thousands of apps. And here are the thousands of collectors.
Where you place the if you have a lot balancer where you place your collectors, is it? Is the collector running on the same node. Is it on a separate namespace? Whatever like trying to diagram that? And like challenges?
Scaling. I don't know.
So you have. We have company company structure kind of to give the reader overview of size. And and who owns what then? Their configuration in the configuration, I'll try to add here, like Let's try to doing a diagram vision.
**Tristan Sloughter** 14:35 Hmm.
**Juliano Costa | Datadog** 14:36 I don't know how to write visually awesome.
It's not like that great spelling.
**Tristan Sloughter** 14:43 Good one s.
**Juliano Costa | Datadog** 14:47 Oh, perfect!
I don't need to be sure.
But let's try to bring a dragon. A diagram show configure. Configurations would be something like Hello there!
Oh, do you think we should so like the configurations? Do you think we should add snippets of actual configuration, or maybe link to a repo where we have know I mean for for I I think here is where we start differing from each company, for instance, for mastodon, I think it would make sense to have in the blog post, because it's 1 collector and one configuration. But Classian may have like different configurations for different types of collectors and.
**Tristan Sloughter** 16:00 Exactly.
**Juliano Costa | Datadog** 16:01 Then, like adding a bunch of config config files throughout the block may kind of just pollute the whole thing.
**Tristan Sloughter** 16:12 Yeah, it.
**Juliano Costa | Datadog** 16:13 Harder. Yeah.
thank you.
**Tristan Sloughter** 16:20 Yeah, it'll be like, how interesting is the configuration, really, the which parts versus the deployment or the structure of a different.
I guess that's yeah question of what people are really looking for, because I don't know that they're well, I guess. No, I'm sure they're they'd be interested in configuration in the sense, you know. Are they using the the disk? Persistence, are they? And what?
Whether number through for batching, compared to the numbers of the flow of the geometry data coming through things like that can be shown through the collector configuration itself. So.
**Juliano Costa | Datadog** 17:12 Yeah, I.
**Tristan Sloughter** 17:13 Snippets.
**Juliano Costa | Datadog** 17:15 I, I think the there is one thing here, like because people are interested of course, people are interested in the the components that they are using. But maybe just listening just listening. The the components on the on on this page wouldn't be too much helpful to be honest, because people are actually interested in kind of examples on how to implement.
And if we omit the config, basically, we are omitting how to implement or not. I I don't know. Like it's it's like for me is one thing saying, Hey, we are doing tail sampling, and a whole other thing to say, Hey, we are doing tail sampling, and here is how we are deploying our collectors. And here is our configuration for tail sampling.
like even the size of the collectors, like on allocation, on resources for for Kubernetes, because the collector need to hold need need needs to to keep the the collector the the traces for for some time before exporting, so you may need some more memory and stuff. Yeah.
**Tristan Sloughter** 18:37 Yeah, ha! Having that sense of, you know, we have this many traces coming through a second and we're doing tail sampling. So we have this many gigabytes of RAM allocated, and our batching sizes are this, and we found it to be efficient. Things like that would be.
**Juliano Costa | Datadog** 18:54 Yeah.
**Tristan Sloughter** 18:55 It was probably the kind of things people are looking for. For. Yeah, that kind of section of of configuration, of processors and resources.
**Juliano Costa | Datadog** 19:13 So I I'll change a bit here. The the outline. Maybe we could kind of bring a diagram as its own section.
**Tristan Sloughter** 19:25 Yeah.
**Juliano Costa | Datadog** 19:26 So like
**Tristan Sloughter** 19:45 You know, there might be.
or less, there might be 2 diagrams, because there might be one that's sort of a higher level of deployments of collectors, and like what teams control them. And then if they're doing anything like tail sampling, there might be a diagram of like flow of telemetry through the collectors, because it's got to be routed to sets of collectors and things like that.
It might end up with 2 per mastodon is probably just one diagram of everything. Medium size.
Sure.
**Juliano Costa | Datadog** 20:25 Idiot, so like any ideas on where we should kind of not where, but like how we should tackle this, because I I think the 1st diagram, showing where the collectors are deployed.
Would kind of show scale and.
**Tristan Sloughter** 20:46 Yep.
**Juliano Costa | Datadog** 20:47 Like how they are deploying the the collector, and then the second one. The diagram of the collector itself would be something more like the autobi right.
like the the flow inside the collector. So the processors and stuff, right? Okay? So I think this second diagram could go on the Configuration section, like the diagram of the collector itself.
**Tristan Sloughter** 21:15 Yeah. And the 1st one could go on company structure really depending.
I mean, if yeah, probably that'd be good and could be its own section as well. But yeah.
**Juliano Costa | Datadog** 22:04 Got it? Oh.
**Tristan Sloughter** 22:05 I'm gonna go feed this cat. So it starts bothering me.
**Juliano Costa | Datadog** 22:10 No worries.
**Tristan Sloughter** 22:12 Hmm.
**Juliano Costa | Datadog** 24:00 Do you?
Do you feel that this is enough?
I think we have a nice flow here.
This is basically what we we discussed last week. But we just had a diagram, and I think wrapping up with pain points and tips is a.
**Tristan Sloughter** 24:25 Skewed.
**Juliano Costa | Datadog** 24:26 Is a good thing.
Though the like 7 and 8 would be something just to get more info from them that we can place on other parts of the the post, but wrapping up with pain points and tips, I think would be would be a nice way to kind of close the the they start.
Sorry.
**Tristan Sloughter** 24:56 Yeah, I think it's yeah. And it's a good idea to pass this along to them beforehand. Of course, to.
They're prepared, and they want to bring anything in particular. They can think about it beforehand.
So yeah, I'll pass this along to the Alassian person and set up an interview to from the coming week or so.
**Juliano Costa | Datadog** 25:25 Okay? So I'll share that with, okay, anyone that has this link is able to access right?
**Tristan Sloughter** 25:35 Yeah.
**Juliano Costa | Datadog** 25:36 This is public. Okay, can I share the this tab?
Yes, cool. Okay.
**Tristan Sloughter** 25:51 That bunch of anonymous things pop up.
**Juliano Costa | Datadog** 25:56 Yeah.
**Tristan Sloughter** 25:58 Frog, turd, duck.
**Juliano Costa | Datadog** 26:02 Am I the duck, or the little part?
I think I'm the duck?
Why not.
**Tristan Sloughter** 26:08 Yeah. So oh, yeah, there's 2 of them.
A 3rd one popped up, too. But yeah.
**Juliano Costa | Datadog** 26:15 Oh, I have it. Okay. Now. I closed it.
**Tristan Sloughter** 26:18 No someone else.
**Juliano Costa | Datadog** 26:22 Yeah, the the more times you open the more users you were.
**Tristan Sloughter** 26:27 No. Yeah.
**Juliano Costa | Datadog** 26:28 Yep.
**Tristan Sloughter** 26:31 There you go!
**Juliano Costa | Datadog** 26:32 Cool. Okay. So I'll share that with Renoke and see if he would like to join, or if someone else from from his team.
**Tristan Sloughter** 26:43 Hmm, okay?
And.
**Juliano Costa | Datadog** 26:49 And yeah, hopefully, we'll have a way to communicate, because looks like we are migrating off slack. So.
**Tristan Sloughter** 27:01 Oh, yeah.
**Juliano Costa | Datadog** 27:03 Let's see.
**Tristan Sloughter** 27:04 Well, I guess we're gonna have. Yeah, we're gonna have free for a bit. I think.
**Juliano Costa | Datadog** 27:09 Yeah.
**Tristan Sloughter** 27:10 While we're transitioning to something new. I guess we'll just talk through free. We just wanna have history. But you know.
**Juliano Costa | Datadog** 27:19 We are losing the the history is painful. But yeah, it's fine but my main concern is like migrating the whole community. So I guess people will continue to use this slack.
**Tristan Sloughter** 27:34 Yeah, unless they could shut it down. But.
**Juliano Costa | Datadog** 27:36 Yeah. Oh, yeah, th-this is.
Hmm, but I don't think you I don't think people actually do that.
**Tristan Sloughter** 27:47 You probably should.
**Juliano Costa | Datadog** 27:47 In demo instances like, Yeah.
let let's see how how that goes. Like I I remember for for Jaeger they they used to have a a different platform, and like they were super active in this other platform and in slack, they weren't active at all. So every time I had a Jaeger question I would raise on Jaeger, and nobody would reply. And then I found out about this other platform, and then started asking there and like, got got answers right away. So yeah.
**Tristan Sloughter** 28:18 Yeah, I'd be worried about discord losing people, because I guess, slack. The reason people use it is they already use it for work. So they're just hopping on to another one. So it it muscle.
**Juliano Costa | Datadog** 28:32 Yeah, it's a way easier to to just navigate from one slack to another.
**Tristan Sloughter** 28:41 And.
**Juliano Costa | Datadog** 28:42 But yeah, let let's see.
**Tristan Sloughter** 28:44 Yeah, hopefully, it works out.
**Juliano Costa | Datadog** 28:47 Cool. Okay? So yeah, thanks. I think we are good for or today.
**Tristan Sloughter** 28:56 Sounds good.
**Juliano Costa | Datadog** 28:57 Awesome.
**Tristan Sloughter** 28:58 Alright, then.
**Juliano Costa | Datadog** 29:00 See you next week.
**Tristan Sloughter** 29:01 Alright sounds good.
Yep.
**Juliano Costa | Datadog** 29:03 Bye.
**Tristan Sloughter** 29:04 But.
