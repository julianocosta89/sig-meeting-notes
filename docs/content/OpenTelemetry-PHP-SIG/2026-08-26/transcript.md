SIG: OpenTelemetry PHP SIG
Date: 2026-08-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak** 04:17 Hey, Bob.
**Bob Strecansky** 04:23 Good day, how are you?
**Pawel Filipczak** 04:25 I'm okay, thank you.
Oh, I am.
**Bob Strecansky** 04:28 Doing alright. Icing my knee, it's hurting.
**Pawel Filipczak** 04:33 What you, what you, what, what you need?
**Bob Strecansky** 04:35 Huh.
What did I do to hurt it? Just being an old man.
**Pawel Filipczak** 04:44 God.
**Bob Strecansky** 04:45 No, tennis takes a toll on your knees sometimes, and… That's just how it goes.
I'm 39, and sometimes I feel 19, and sometimes I feel 59.
**Pawel Filipczak** 05:01 I'm 4 to 5, so… A bit more, but still.
In my head, I'm still, you know, 20.
**Bob Strecansky** 05:09 Depends on context.
I'm going out with some of my college friends this weekend to New York City. I have a feeling I'll probably feel more 19 and 59 at some points of that weekend than others.
**Pawel Filipczak** 05:23 Yeah.
Oh, sorry.
**Bob Strecansky** 05:29 We'll wait for, Chris, maybe give it 2 more minutes.
**Pawel Filipczak** 05:35 So, how is it going? Is it still summer or autumn?
**Bob Strecansky** 05:38 Ugh, it's still summer for sure. Like, yesterday… at… I walked to pick my daughter up at… Of, like, 5.30, and it was… 38 degrees Celsius outside?
And, it's very, very humid here.
So, you go outside and it kind of feels like a hair dryer.
**Pawel Filipczak** 06:01 Wow, wow, crazy.
**Bob Strecansky** 06:03 Yes.
We definitely…
**Pawel Filipczak** 06:05 It's 20.
Maybe 21?
1 or 2 hours, then it's… during the night, it's… it's close to 10, so…
**Bob Strecansky** 06:14 It's too cold.
**Pawel Filipczak** 06:15 Yeah, man beats. I'm beats.
**Bob Strecansky** 06:19 Are you in… you're in… I know you're in Poland, where in Poland are you?
**Pawel Filipczak** 06:22 north of Poland, in the mountains.
**Bob Strecansky** 06:24 solid.
**Pawel Filipczak** 06:25 Yep.
Just in the middle of North.
**Bob Strecansky** 06:28 Got it.
**Chris Lightfoot-Wild** 06:29 Cool.
**Bob Strecansky** 06:30 Hello, Chris!
**Pawel Filipczak** 06:31 Hey, Chris.
**Chris Lightfoot-Wild** 06:32 Talk to the delivery.
**Bob Strecansky** 06:33 No sweat.
**Chris Lightfoot-Wild** 06:35 Came to the laptop and decided not to work.
Oh, we're off.
**Bob Strecansky** 06:38 It is the year of the Linux desktop.
Alright, so let's get… we have a couple agenda items today. If anybody else has agenda items to add, feel free to do so. But I'll get started with my agenda items.
First one was this OpenTelemetry community issue that Jerry opened and has been fighting back and forth with for a month to try and get a repository set up for the OpenTelemetry PHP operator.
It's annoying to me that it takes this long for this to happen and have this much… argument, and, like, I think that's just… it just shows that… we need to have more stewardship, just in general, but oh well. So, that's… going in a positive direction, even though it's been a pain in the neck. So, I feel for Jerry.
Here we are.
**Pawel Filipczak** 07:30 There you also opened the PR with the… in the country repository, right?
**Bob Strecansky** 07:35 He did, yeah, I think that's, like, the one in the… the one in the contributor repository, I feel like, is… it's fine, but it's just a stopgap to try and accomplish what he really wanted to accomplish with the operator, but… It may be adequate.
The other things that I wanted to bring up are Mary's AI post. Did y'all see that post in… I think I shared it on our channel with,
**Chris Lightfoot-Wild** 08:01 Yeah, I had to read through.
**Bob Strecansky** 08:03 Yeah, where is it? Php Admins… yeah, this one.
about, AI workflows.
I can…
**Pawel Filipczak** 08:12 see anything.
**Bob Strecansky** 08:13 Say it again?
**Pawel Filipczak** 08:14 I can't see anything on the.
**Bob Strecansky** 08:16 Oh, that's right, I'm sorry, I was just sharing my…
**Pawel Filipczak** 08:18 bar.
**Bob Strecansky** 08:18 Yeah, I'm sorry, I was sharing my, Just my… I'll share my whole screen, one second.
They are conceded.
Now you can see Mary's post here about,
**Pawel Filipczak** 08:31 Damn.
**Bob Strecansky** 08:32 about banning it… not banning AI, but trying to… I mean, it's… I feel like it's the same stance that almost every company in the universe is having now.
Be cautious, be careful.
But we're not gonna ban it, you know, it's… It is what it is.
So…
**Chris Lightfoot-Wild** 08:50 Jim is not, like, some sort of workflow, maybe that's what they're looking into, but where it'll just tag it going, like, this little suspect.
Okay.
**Bob Strecansky** 08:57 Yeah, maybe… maybe so. I think, Yeah, I… I agree with you. It's one of those things, right? Like, We know that AI is going to be an important part of our work over the next 1, 5, 10 years, but how it plays a role and where it plays a role will be very fascinating.
**Chris Lightfoot-Wild** 09:19 Yeah.
**Bob Strecansky** 09:21 I think that's the nicest way to say it.
**Chris Lightfoot-Wild** 09:26 And the gist seemed to be that it was kind of okay then, like, if we do have a bad feeling about something, it looks like a… like, you know, AI-generated thing, and no one's being honest about it, and just avoiding the… like, we can just close it.
**Bob Strecansky** 09:41 Yeah, I think… I mean, I think give… we are given the autonomy to do what we feel is right for the SIG, and what we feel is right for the SIG is to close down slop PRs, and that's fine. I think… We haven't really faced this a ton in our SIG yet, but I have a feeling we will face it more. It's just, like, people wanting to quickly fix something that fits their agenda. I think we have to be diligent about making sure that we don't let in garbage, but it's garbage in, garbage out.
So, that's always a goofy conversation, but here we are.
Alright, next, Trask had a, He had a PR… he had a PR that he wanted us to take a look at here with, semantic conventions.
I was talking about the PHP slam and guzzle PHP HTTP conformance.
I haven't had a chance to read through this yet, but I'm sure that I will.
**Pawel Filipczak** 10:38 I did it, so it looks good. Okay. It already catch some missing fields, but I think, as a follow-up, we can extend it with the curl and PSR18.
Yeah.
And, yeah, that's… that's… how it, how, how it works, it's… it's quite thin. I mean, the design of the tests are quite thin, so… Yeah.
**Bob Strecansky** 11:08 But, like you said, Tina.
**Chris Lightfoot-Wild** 11:09 I didn't even realize that that repository existed.
**Bob Strecansky** 11:13 Yeah, it's relatively…
**Chris Lightfoot-Wild** 11:14 Like, no.
Yeah, it's my brother.
**Bob Strecansky** 11:16 Relatively new.
**Chris Lightfoot-Wild** 11:19 Like, should each SIG be… Contributing its own bits to it, or is it… how does it kind of work?
**Bob Strecansky** 11:26 I think… I don't know I've heard them talk about it at the maintainers meeting, but there hasn't been, like, a call to action to have active contribution. Maybe they're just trying to, like, get it set up, and then eventually SIG owners will… Work on it.
And, maybe improve it, or whatever. To me, it's almost good if you have that as, like, a separate body of work with separate people.
Besides the people that work on the SIG.
Because then it's, you know, it's an unbiased opinion, and perhaps it's the right thing to do.
I don't know. I have… I have lots of opinions, but I don't feel like I need to share any of them, because I feel like they're all pretty common opinions.
Okay… What else we got on here? I think that those are all of my agenda topics. Y'all have stuff you want to talk through?
**Pawel Filipczak** 12:25 For Zero tasks, so… yeah.
**Bob Strecansky** 12:27 I might say it again.
**Pawel Filipczak** 12:28 I have just regular tasks, so I made some contributions to the distro, so please guys take a look in the PRs in the distro.
So now I'm alone with Ozergy, so… yeah.
I'm camping on you to, to just…
**Chris Lightfoot-Wild** 12:47 My pleasure.
**Pawel Filipczak** 12:48 Or something is not clear, please just ask me.
So… What I implemented recently is the header capturing in the root span, in the distro.
And if it's okay for you, then I will follow up and do that also for the SDKs, Rutsman implementation.
then I will try to reuse the SDK through Span in the distro, but it's not so easy.
So I will just make it as a… as a next… next issue, and some… somewhere in the future.
Sylvium.
And I also analyzed the fix in the extension, the current, the regular instrumentation repository.
And this fix with the WIFspan attributes, it looks good, so it can be merged, in my opinion. So I spent a bit of time analyzing how the data is being allocated and freed by the PHP in China.
It, it looks safe.
**Bob Strecansky** 13:54 Let's… let me find that PR so I can also review it later, just… That was in, you said instrumentation?
**Pawel Filipczak** 14:04 In the instrumentation.
**Bob Strecansky** 14:07 Alright, pull request… Trying about this one?
**Pawel Filipczak** 14:13 Yes,
**Bob Strecansky** 14:16 Snowy Sailor.
**Pawel Filipczak** 14:18 No.
**Bob Strecansky** 14:21 Alright, I'll take a look at that later and see. Whoa!
Got it there.
Okay.
Yeah, I'll take a look at that. Today…
**Pawel Filipczak** 14:36 So, and the last thing is the semantic conversions update in the country repository, so I made a update, so I'm… Drop the trace attribute, namespace, and use this… new ones, like HTTP, database, attributes, and so on. So… Please take a look into that.
Oh.
He's, he, he's… I'm not sure if we need that update, but during some, you know, next updates of the semantic conventions, they will be dropped.
Probably so, I wanted to just update… I added the country repository.
So, yeah.
**Chris Lightfoot-Wild** 15:22 look at that. I noticed there was 60-odd files, and I thought, I'll come back to that.
**Pawel Filipczak** 15:26 Yeah.
I wanted to split it into separate packages, but then I realized that it's just the same changes, so it's quite Outdoor.
**Chris Lightfoot-Wild** 15:37 Sorry, I'll have a look through, I just thought, like, oh, yeah. Oh, it's grown a lot, maybe my memory was bad.
**Pawel Filipczak** 15:46 Yeah, it's a lot of files, a lot of changes, but all of those changes are just the same, so I just… Try to find the attributes for the customs, custom strings attributes, and they appeared in the semantic convention during the time.
And so, yeah, but still, we have some customs there.
But it's just so pure.
No.
**Bob Strecansky** 16:16 Excellent.
Thank you, bro.
**Chris Lightfoot-Wild** 16:19 We're gonna go through the board, because there was one in particular I wanted to flag, which was one of Nive's PRs in Contrib.
**Bob Strecansky** 16:27 Okay, we'll walk through.
**Chris Lightfoot-Wild** 16:29 Cool.
Not that there's an issue with that, just the Zizmo workflow.
**Bob Strecansky** 16:36 Yeah.
Gotta read some of these.
You… you said… oh, you said the one that… I got… yeah, I have to check, I have to go through some of those that are just hanging out.
Let's see, you said income triv…
**Chris Lightfoot-Wild** 16:54 Yeah.
**Bob Strecansky** 16:56 Hmm… you said bye…
**Chris Lightfoot-Wild** 17:00 But the context preserving, that's it, yeah.
Now, I think the workflow is being… sorry, it's been blocked by the Zismo workflow, maybe not… running, because it's not in main, or it's not in main merged into it or something? I couldn't… I couldn't merge it.
**Bob Strecansky** 17:16 Okay, let me take a look.
**Chris Lightfoot-Wild** 17:17 I don't know if you've got, like, More privileges to just… Oh, we need to ask him to merge, man.
**Bob Strecansky** 17:23 -Oh.
Wait, I'm sorry, one more time?
**Chris Lightfoot-Wild** 17:27 I don't know if you can either merge it, or we need… This one? Leave it.
Yeah, we might need Niva to rebase onto Man, or…
**Bob Strecansky** 17:36 Yeah.
**Chris Lightfoot-Wild** 17:37 Get the workflow working.
**Bob Strecansky** 17:39 Did we get Zizmor installed in this repo? I think so.
**Chris Lightfoot-Wild** 17:43 Yeah, so now I think it's blocking everything that's not had main merged in.
**Bob Strecansky** 17:47 Okay, let me double check.
**Chris Lightfoot-Wild** 17:54 What's up?
A different thing, I think.
**Bob Strecansky** 17:57 Yeah, I know, I was just looking on a different PR to see… like, that one has… there's more as code scanning results. I wonder if we can just re-trigger Nivea's PR.
**Pawel Filipczak** 18:08 You can close and reopen PR then, it should be…
**Bob Strecansky** 18:12 Yeah…
**Chris Lightfoot-Wild** 18:37 Is… is Zizmo in that list, then, I guess?
What do you need to know.
**Bob Strecansky** 18:41 Yeah, it is.
**Chris Lightfoot-Wild** 18:42 Sweet.
Oh, if it was only… There you are. The more you know.
**Bob Strecansky** 18:49 I bet you if you re-triggered the GitHub's actions too, it would have done the same thing, but whatever.
**Chris Lightfoot-Wild** 18:54 I tried, but I was on my… yeah, maybe being on my mobile didn't help, because I was gonna…
**Bob Strecansky** 18:59 On your mobile.
**Chris Lightfoot-Wild** 19:01 It's a dumbs-down version of the eye, is it?
**Bob Strecansky** 19:04 Okay, we'll wait for that one to come… you know, I'll pin that one, too.
Alright.
**Chris Lightfoot-Wild** 19:11 I was interested in that one, because that was going to be a new repository, and that would test the workflow, to trigger one automatically.
So, kind of keen to see that one go through.
**Bob Strecansky** 19:23 Cool.
We'll get it. We'll get it through.
There's a couple other ones in here that we need to walk through to, I'm sure.
Alright… And instrumentation…
**Chris Lightfoot-Wild** 19:43 You had one of your own as well, Bob, which was… Stalebot? But there was a thing on there from Zizmo saying, don't know what this reference is?
**Bob Strecansky** 19:52 Oh, is that it…
**Chris Lightfoot-Wild** 19:53 Copied as an example.
**Bob Strecansky** 19:55 Hold on, that was in the main repository, right?
**Chris Lightfoot-Wild** 19:58 Yeah. It's got this, like, rogue commit that… don't know where that's come from.
**Bob Strecansky** 20:03 This one?
**Chris Lightfoot-Wild** 20:05 Yeah.
**Bob Strecansky** 20:11 Yeah, I don't know what happened there.
Hmm.
Let's see, I'm gonna do…
**Chris Lightfoot-Wild** 20:21 I didn't go to that, stale repo, and I couldn't find that in the tree, so…
**Bob Strecansky** 20:26 Let's just…
**Chris Lightfoot-Wild** 20:27 That's that example.
**Bob Strecansky** 20:29 It's weird that this is more, thing is successful.
Did you approve this? No, if you can approve it, I bet you we can merge it still.
**Chris Lightfoot-Wild** 20:41 It won't work, because the commit doesn't exist.
**Bob Strecansky** 20:44 Yeah, that's very strange.
Oh.
Is it this… I got this action still from somewhere, let me double check that this is… Right one.
**Chris Lightfoot-Wild** 21:13 We can just use that 4391 count, I suppose.
**Bob Strecansky** 21:17 There we go.
**Chris Lightfoot-Wild** 21:18 The one that's the 439 over there, we can use that one.
**Bob Strecansky** 21:22 That one, let's do that.
I wonder…
**Chris Lightfoot-Wild** 21:28 Just in the URLs out there.
**Bob Strecansky** 21:29 Yeah, but that's the short one. Can you use that one, or do you have to use the long one?
**Chris Lightfoot-Wild** 21:37 I wouldn't… I think it… I think you have to use the fully qualified one, but…
**Bob Strecansky** 21:41 Yeah, where do… let's see, where do I find that?
**Chris Lightfoot-Wild** 21:43 The, page you are talking about.
**Bob Strecansky** 21:45 Oh, yeah. Sorry, Zoom is in the way.
**Chris Lightfoot-Wild** 21:49 No, sorry, yeah, I can't see your Zoom.
But…
**Bob Strecansky** 21:55 Yeah, let's see, okay, so let's go back here and see if we can go back… where was that?
**Chris Lightfoot-Wild** 22:02 And I guess the only other bit was we need to… Fill out the, boilerplate messages.
**Bob Strecansky** 22:08 Yeah, probably so.
**Chris Lightfoot-Wild** 22:09 But it… should it work? Just wary that it would go and post on a bunch of these PRs saying… some generic thing.
**Bob Strecansky** 22:16 Yeah, probably so, that's, let's edit this real quick and see if that makes a change.
Come on, Zoom, get out of my way.
There we go.
Let's see if that doesn't.
Ugh, not updating sheets, updating sure.
Thanks.
Alright, well, we'll see if that works.
Alright, let's see how our install base is looking… Almost to 50 million, that's exciting.
Whoa.
PHP versions are people using?
Mostly… 0.3.
It's kind of surprising.
Whoa.
**Chris Lightfoot-Wild** 23:51 So mostly everyone's on 8.3.
**Bob Strecansky** 23:53 That's what… that's what it looked like.
34%, 35, so a third?
Cool.
Anything else?
**Chris Lightfoot-Wild** 24:07 I guess we could do with tagging some contra packages soon, I've not done it for a little bit.
**Bob Strecansky** 24:13 Oh, you're talking about the Renovate one?
**Chris Lightfoot-Wild** 24:16 No, just going through and stamping out some new tags.
**Bob Strecansky** 24:20 Oh, yeah, yeah, yeah, sure.
**Chris Lightfoot-Wild** 24:22 I suppose I could try and get some… yeah, I can try and look at some of the renovate stuff, but I don't have that much faith in a lot of the renovate ones, because they don't… They don't even have faith in themselves at times.
**Bob Strecansky** 24:31 Yeah, it's coming down.
**Chris Lightfoot-Wild** 24:32 I believe says, we're not that confident in this, and then…
**Bob Strecansky** 24:35 Yeah, I have… I have such, A love-hate relationship with those, because it's like… I know that we need to do those updates, but it's just, like, annoying to do them, and it just feels like init… nothing. Big nothing burger.
**Chris Lightfoot-Wild** 24:49 Is there, like, a better way… so if I see one, I think, oh, this is just… it needs work, like, it's kind of highlighted that there's an update, but it's not going to work as they've done it, and it just becomes a work item, then, for us to try and look at. If we just close it off, does that never come back again for that?
dependency, because.
**Bob Strecansky** 25:07 No, I think I've seen ones that I've closed come back later, just like when the next version of the package comes out.
**Chris Lightfoot-Wild** 25:15 I mean, maybe it's okay to do that for a little bit, then?
**Bob Strecansky** 25:18 Yeah.
**Chris Lightfoot-Wild** 25:18 generate a lot of noise, and it's like, well, I can't… I've had time to go through 10 different PRs.
**Bob Strecansky** 25:24 I would say the renovate… PRs are important, but I wouldn't lose… A, I wouldn't lose any sleep over them, and B, I wouldn't prioritize that over any other work.
That's just, like, if you have a couple minutes and can make sure that they're alright and then merge them, that's fine, but… At least that's my opinion, maybe a security research might… a security researcher might say something different, but… That's… that's how I feel about them.
Okay.
**Chris Lightfoot-Wild** 25:56 I missed the very first thing you had, but were you in different surroundings? Have you got, like, a chill-out area at work, or are you at some sort.
**Bob Strecansky** 26:03 Oh, yeah, I'm working from home today, my, I'm… I see my knee.
**Chris Lightfoot-Wild** 26:09 Oh, are you okay? Yeah, just…
**Bob Strecansky** 26:11 Old man.
**Chris Lightfoot-Wild** 26:13 An old tennis injury, come back to.
**Bob Strecansky** 26:16 Yeah, the tale as old as time. Father time wins every time.
**Chris Lightfoot-Wild** 26:20 Nice. Yeah.
**Bob Strecansky** 26:21 But there aren't just need to… just need to follow the old, acronym, RICE, Rest, Ice, Compression, Elevation.
**Chris Lightfoot-Wild** 26:30 That's nice, well, hope it, is on the mend for you.
**Bob Strecansky** 26:33 It is.
Alright, gents, we'll see you next week.
**Chris Lightfoot-Wild** 26:38 Cheers. See you later.
**Bob Strecansky** 26:39 I know.
