SIG: Project Tooling SIG
Date: 2025-10-02
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/d4BOzhXZvULS3l8GbCD-aPLfGOhMM4YIt4ZMYC-QoRkED7RzpXfnw-x_jWiL1oTj.NuG2vid_hvmDV69k
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:23 Hey, hey.
**Austin Parker** 00:31 I'm unmuted, yeah.
**Trask Stalnaker** 00:33 Yeah, yeah, I hear ya.
**Austin Parker** 00:38 I was just replacing switches on my keyboard.
With the old ones.
The new ones.
**Trask Stalnaker** 00:49 New caps, or just new…
**Austin Parker** 00:53 Switch, new switches.
**Trask Stalnaker** 00:54 Oh, the switch is installed, okay.
**Austin Parker** 00:56 So, I switched to a low-profile keyboard. It's more compact, so that my hands wouldn't have to move as far, or move, like, shift as much.
But it came with the… These, which…
I don't know if you can hear it.
**Trask Stalnaker** 01:16 No, it's… it's canceling.
**Austin Parker** 01:18 Yeah, it's canceling… yeah, it's canceling.
**Trask Stalnaker** 01:20 They're really good at noise cancellation. Yeah, my keys are…
**Austin Parker** 01:24 Okay.
**Trask Stalnaker** 01:25 What about… Thank you.
Yeah. Yeah, yeah, yeah, yeah.
**Austin Parker** 01:31 You can hear it now?
**Trask Stalnaker** 01:33 Yeah, yeah.
**Austin Parker** 01:33 Okay, so this is the old one.
But this is the new one.
**Trask Stalnaker** 01:41 Do you hear the difference?
**Austin Parker** 01:44 There's… There's definitely a difference.
**Trask Stalnaker** 01:47 Yeah, yeah, no, I believe you.
**Austin Parker** 01:48 It's… it's maybe not, like…
it definitely feels a lot like… this one hasn't… doesn't have a bump, really. Like, I like the… this isn't super tactile, but the new ones have just, like.
It's very faint, but it's there.
And you can definitely hear it, I guess not through Zoom so much. But anyway…
I got, like, 10 of them, because I wasn't sure about them, and then I, like, put in…
two or three, like, the modifiers, and then I even tried it, and I was like, oh my god, this is night and day, and so, like, immediately went out and bought, like, another 50 so I could swap them all out.
But…
Yeah, my big thing for my break was, like, trying to deal with some, like, ergonomic stuff, because my hands have just been, like… my hands and wrists have been really bad, so, like, I switched to…
Like, the vertical mouse?
**Trask Stalnaker** 02:41 Oh, okay.
**Austin Parker** 02:43 Like, it's this one, because, like, you know, you don't do this, you do this.
Yeah.
And… Yeah, anyway…
**Trask Stalnaker** 02:51 Mousy sucks.
Mousing sucks, that's why I have two mouses. I… I… a bide dexterous mouser.
**Austin Parker** 02:59 I usually have… I've been a trackpad person, like, because mice, like, normal mice did give me the cramps, but then… but, like, trackpads didn't, but now, like, it's starting to get, like, right through here, like, from the…
Like, all of this?
**Trask Stalnaker** 03:16 Clicking, yeah.
**Austin Parker** 03:17 Well, from, like, the moving your, like, the finger movements?
And so I'm hope… and so, with this.
I'm moving, like, it's more like the elbow and the shoulder.
move the mouse rather than the hand, so the hand kind of just stays at rest. My goal is… I'm getting, like, a little…
I think this is the… the split keyboard?
**Trask Stalnaker** 03:40 Oh, yeah, yeah, yeah, yeah.
**Austin Parker** 03:42 And… There's a little plate you can put on, like, this back plate is magnetic.
But there's a magnet with a, like, that you can get, that they will sell you, that goes on here, that has a normal…
Like, screw, or… Like a… like a tripod screw.
**Trask Stalnaker** 04:09 Okay, yeah, yeah.
**Austin Parker** 04:10 mount. And so I'm getting that, and I'm gonna put it onto these clamps, and then I clamp it to the desk.
And so… and then I can just position it however I need to, so I don't really have to move my… it's like, I'll be able to get it set up to where…
like, the keyboard will just be, like, here, and then I just move, like, my shoulder, my arm, instead of having to, like, rotate…
my hand at all, or my wrist, I can just kind of move my arm over to get the mouse and not… and avoid, sort of, like, the wrist and finger bend and strain.
That's the goal, at least.
**Trask Stalnaker** 04:45 Cool, I went through about a… year ago, I finally…
I went keyboard shopping, because I'd literally had the same keyboard for 20 years.
Because I had this tent… it was a tinted keyboard, it was, like, it was just perfect. Yeah.
**Austin Parker** 05:05 Was it one of the Microsoft ergonomic ones? Because those were good.
**Trask Stalnaker** 05:09 No, it was actually tinted, like, like, you could kind of pull the.
**Austin Parker** 05:15 Oh, you could adjust it.
**Trask Stalnaker** 05:16 just the tenting?
**Austin Parker** 05:18 Yeah, yeah.
**Trask Stalnaker** 05:18 So I would tent… I had it tented pretty much max, like, at about, I'd say, like, this…
goal.
And I loved it, but, like, like, 20 years later, like, the keys were, like, I was like, oh, these are kind of getting sticky, like, I cleaned it, like, they just, like, were, like, a little too much pressure to push on.
Yeah. So I went through, at Best Buy, like, 10… I bought, like, 10 different keyboards over a month and a half, and finally found one that made me reasonably happy.
**Antoine Toulme** 05:55 How are your wrists.
**Austin Parker** 05:58 Yeah, but I'm… I'm looking forward to getting the… getting everything situated…
Anyway, yeah, so what's the deal with Gradle?
**Trask Stalnaker** 06:13 Yeah, so the Great Old folks got back to me, they said it's that CAA record.
**Austin Parker** 06:20 Of course it is.
**Trask Stalnaker** 06:21 I put it on the, if you want to pull up that, community issue, I put their response on there.
Let me find it…
They said, the CAA record in place prevents us from using Let's Encrypt to create certs.
**Austin Parker** 06:41 Why? Because we have a CAA record for Let's Encrypt.
Is it because of the…
**Trask Stalnaker** 06:53 These are removed so that DNS allows let's Encrypt. I think it should resolve the issue, is what they said.
**Austin Parker** 07:06 I'm gonna assume… Or actually, let me… Know what Assumption does.
Let me look at something,
So, we have…
Okay…
My… gut feeling here is I don't quite know what this…
account URI equals whatever is, but my assumption is that it means that only… Netlify, or whoever…
can make a… Acme signing request.
And if that's the case, then theoretically, we should just be able to drop the account URI part, and have things still work?
**Trask Stalnaker** 09:34 What was the, what was the CAA that was something recently added to address the go…
**Austin Parker** 09:42 Well, no, the CAA was originally added because someone filed a vulnerability that we didn't have one.
Which meant that anyone could issue certs for the hotel.io domain, which, turns out was actually, you know, something that we used. So, I'm also just as inclined to…
Delete both of these things and be like, the only way someone could ever do this is if they hijacked
the DNS… They would have to, like, literally take over our DNS and create subdomain records.
I'm not… Like… At that point.
**Trask Stalnaker** 10:33 Couldn't, what about Man in the Middle?
If they can…
**Austin Parker** 10:37 I don't think it matters.
I mean, I don't think that would…
I understand, I under…
Not a security person, not a DNS person, not a cert person. My understanding is the way that Let's Encrypt works is that
It… like… Y-you have to ha- like…
Let's Encrypt side has to verify that you're… That you control the domain.
that you're trying to create a cert for, or that you control, like, the APEX domain?
So… I don't think there could be any kind of, like, man-in-the-middle thing happening, because…
you wouldn't be able to change Let's Encrypt's DNS?
like, because it's the remote, you know, it's the DNS from their side. They have to see the whatever, so if you… if someone did set up, like, I don't know, a DNS proxy that proxied www…
Then it would… I don't… I don't know, I've never…
Yeah, so…
**Trask Stalnaker** 12:01 Say that again.
**Austin Parker** 12:01 Account URI narrows which lets Encrypt Acme account is allowed to issue. It doesn't affect other CAs, other issuers…
are blocked or allowed by issue, IssueWild. So, yeah, specifically…
Specifically, what it currently is set up to do, is…
it only… basically, the only Let's Encrypt certs that can be issued against the domain right now are ones from Netlify.
So, to… What we would need is another… CAA for their thing.
**Trask Stalnaker** 12:46 Oh, can we… do that… have the CAA scoped to the… You can have multiple.
**Austin Parker** 12:52 ones.
Like, that would be the, I think, best way to do it, is…
**Trask Stalnaker** 13:01 Sounds like a good option.
**Austin Parker** 13:04 Yeah.
Because then, because that, I mean, if we are going to continue down this road, then it just means that any time…
someone else wants to issue a cert on our behalf, we would need to add their… we would need to add a CAA record.
were there, let's encrypt account URI, or whatever.
**Trask Stalnaker** 13:28 Yeah, I should also add… Do we need…
Do we even need, a domain… subdomain for this?
Gradle.
**Austin Parker** 13:42 That I don't…
**Trask Stalnaker** 13:43 And is it just a vanity URL?
**Austin Parker** 13:45 I mean, it seems like a vanity URL to me. Like, I don't know…
**Trask Stalnaker** 13:48 In which case…
**Austin Parker** 13:49 I did not know this existed until someone brought.
**Trask Stalnaker** 13:51 Yeah.
Okay, let me check that first.
Because if it's just a vanity URL, seems easier to just… Not have it.
But if we do need it, then that…
Scoping the CAA sounds like a good plan.
**Austin Parker** 14:14 Yeah.
Yeah, if, if… I think the e… the best thing would be…
Yeah, so look at… so…
GPT-5, admittedly, says that if we drop the account URI, then we remove the account level PIN
Let's Encrypt could still issue certs, but any Let's Encrypt account could issue a cert for the domain?
I don't necessarily think that's, like…
the end of the world? Because I think there's probably other stuff on here that…
like, I don't know, like, I imagine.
**Trask Stalnaker** 14:57 Oh, yeah.
**Austin Parker** 14:58 he's…
**Trask Stalnaker** 14:58 I just like to limit our, operational overhead.
**Austin Parker** 15:03 Yeah, no. No, I mean, I think that's fair.
**Trask Stalnaker** 15:09 Given that none of us.
**Austin Parker** 15:09 I think, like, we'll probably see a similar issue if we haven't already, with, like, get.opent.io, scarf stuff.
For the same reason? Or, like, docker.opentelemetry?
**Trask Stalnaker** 15:23 Oh, we have docker.openTelemmetry?
**Austin Parker** 15:25 We do, but I bet it doesn't… but I bet if it…
I surmise that these are probably also broken in the same way.
**Trask Stalnaker** 15:33 Yeah, once… once the cert expires.
**Austin Parker** 15:36 Yeah, and those are all, like, 90 days, you know, I think LE starts at 90 days by default, right? So…
It's… they're probably all… Broken or about to break.
**Trask Stalnaker** 15:51 What's Docker OpenTelemetry used for?
**Austin Parker** 15:55 I don't even know if we actually went through with it, but it's a proxy for, it's a proxy to Docker Hub.
hotel, so you could do, like, docker.opensor.io forward slash whatever.
And get the underlying… Docker Hub images back.
We're using it for, like, scarf analytics. I don't think we ever actually finished implementing all of that.
**Trask Stalnaker** 16:24 Oh, it was… that was part of the scarf stuff.
**Austin Parker** 16:27 Yeah, I think it kind of got… I don't think anyone ever… Finish the work.
**Trask Stalnaker** 16:39 Cool, I gotta go.
**Austin Parker** 16:41 Okay.
I don't really have anything else. Antoine, did you… have something you want to talk about?
**Antoine Toulme** 16:51 Hey, Austin, I need you for something else entirely, which is that there is a blog post for the observatory.
And so we just need to make sure we, I put some time…
I invited you to a meeting at 2.30 today, if you would like to join.
And… If you cannot join, that's fine, that's life. I just want to ask you…
**Austin Parker** 17:13 And join.
**Antoine Toulme** 17:14 if there is a spreadsheet for the schedule, or, we might want to talk about that. Like, I know last year you kind of did the shepherding work of going to every meeting and telling people about it.
**Austin Parker** 17:29 Let me…
**Antoine Toulme** 17:29 Let me show you what I'm talking about.
**Austin Parker** 17:30 5.30. Okay, 5.30 is not good for me.
Oh, wait, are you East Coast? I'm East Coast, yeah.
**Antoine Toulme** 17:38 Oh, I'm so sorry.
**Austin Parker** 17:41 So, usually, the end-user SIG, does the scheduling stuff, so, like, Ariana and Reese.
**Antoine Toulme** 17:48 Oh, okay, who would be the right people for this? Not…
**Austin Parker** 17:51 I… Adriana and Reece usually handle this stuff. I, I haven't gotten to the point of saying, hey.
you should go do that, but I will… do that.
**Antoine Toulme** 18:06 bring them into that meeting, maybe?
**Austin Parker** 18:13 I take it you are interested in working on this?
**Antoine Toulme** 18:16 No, the… I'm on the observatory, right? So we have a blog post that's coming out, and they're asking us… the blog post needs to be out by tomorrow for some reason, which I… okay, sure, whatever. There's no mention of the observatory in the blog post right now. Should we make a mention of it?
**Austin Parker** 18:32 Which blog post is this?
**Antoine Toulme** 18:34 OpenTeetry.io.
**Austin Parker** 18:36 Okay, let me go to…
**Antoine Toulme** 18:38 Let me bring that up to you so you can see it here in the chat, maybe?
**Austin Parker** 18:43 Yeah, I'll just… let me go look, it's in the PRs?
**Antoine Toulme** 18:46 Yeah, the PR itself, yeah.
**Austin Parker** 18:48 What PR number, or…
**Antoine Toulme** 18:50 7968.
**Austin Parker** 18:51 Oh, I see it. QCon 2025 blog post.
**Antoine Toulme** 18:54 So she's working on that right now, and she was asking, hey, what do we say about the observatory? Like, well, I'm…
We should very much reuse what was said last year.
The only big problem is that it links to a spreadsheet which is the wrong one, because it's last year's.
So can we… we don't have to get the spreadsheet ready by tomorrow, that'd be crazy, but can we… I like what the blog post says, it's like, we have…
Those fresh is being worked on, or, like, it's not quite ready yet, but check back later, right?
**Austin Parker** 19:24 Yeah, that's nuts.
**Antoine Toulme** 19:25 Screw this placeholder.
**Austin Parker** 19:26 Just… When did we do this last year? I feel like…
**Antoine Toulme** 19:31 Much later.
**Austin Parker** 19:32 Yeah, like, this seems like we're doing it very early.
**Antoine Toulme** 19:36 Extraordinary, yeah, agreed.
**Austin Parker** 19:40 Let me just drop some comments on that ER thread.
**Antoine Toulme** 19:44 You got it.
**Austin Parker** 19:45 This…
**Antoine Toulme** 19:45 It helps… Yeah, and morgan's out, so I didn't get a chance to talk to him about, like.
what we are doing for the observatory together this time around, so I'm actually not up to speed.
So… We can figure that out, that'd be cool.
Yeah, I saw you hopping on the infrastructure meeting, I was like, oh…
I need to talk to that guy.
And that's mostly it, I don't want to impose on your time more than that.
**Austin Parker** 20:42 That's fine, I'm just…
Okay, I posted a comment on that PR thread.
**Antoine Toulme** 21:30 Okay.
**Austin Parker** 21:31 So, I, I…
Yeah.
And I'll,
I'll just touch… I'll touch base this week with the end user SIG, just to make sure that…
you know.
We're all on the same page, but yeah, usually we don't…
I mean, I guess we're getting close to the time when we would usually start figuring it out, but…
**Antoine Toulme** 22:03 That's early, right? I mean, it's just that?
**Austin Parker** 22:06 It just feels like, yeah, usually it all comes in significantly hotter than this, but, you know, there's always a lot going on.
I'll check with them and, get the ball rolling there.
**Antoine Toulme** 22:21 Oh my god, god, crap. I was just thinking, maybe, if nothing gets better, we can just build a spreadsheet for now, even if it's completely empty, and at least we get…
**Austin Parker** 22:30 Yeah, you could duplicate that existing one…
**Antoine Toulme** 22:34 I don't… I don't have access to it, I can't copy any.
**Austin Parker** 22:36 No. Well, I… I… my thought for now would be, like, we can always just make a separate blog post closer to the event when we have the schedule locked in.
**Antoine Toulme** 22:45 Okay.
You got it.
**Austin Parker** 22:47 Okay.
**Antoine Toulme** 22:50 Okay, awesome. Thanks.
**Austin Parker** 22:52 No problem! Alright.
**Antoine Toulme** 22:53 Have a good one.
**Austin Parker** 22:54 Cheers.
