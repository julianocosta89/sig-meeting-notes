SIG: GO SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 01:59 Hey.
How y'all doing?
**Robert Pająk (Splunk Inc.)** 02:13 Hello.
**Tyler Yahn (Splunk)** 02:15 8.
Brandon, Long time to see.
I don't know if you can hear me.
Can you hear me, Robert?
**Robert Pająk (Splunk Inc.)** 02:26 Yes, we can, we can do it.
**Tyler Yahn (Splunk)** 02:28 Oh, okay.
I gotcha.
Yeah, it's getting dark for you. Bryan's probably even darker, right? He's for the north.
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 02:40 Yes.
public doc.
**Tyler Yahn (Splunk)** 02:44 Yeah.
When's… you guys already did, the time change, or is it next week?
**Bryan Boreham (Raintank, Inc. – Grafana Labs)** 02:50 No, it was… it was last week. We… we went an hour… a week earlier.
**Tyler Yahn (Splunk)** 02:54 Oh, that's right. Okay. Yeah.
Yeah, that's a… it's probably my least favorite time of the year, right now.
Of course, I'm traveling to Salt Lake City, which is, like, that extra hour that I just.
**David Ashpole (Google LLC)** 03:09 Gotcha.
**Tyler Yahn (Splunk)** 03:09 sort of… I'm gonna be adding it up back on, so it's like, great, I get a whole week of… Flipping back and forth, so, yeah, not a lot of fun.
What's up, David?
Yeah, I'm guessing it's gonna be a pretty, light weekend, or a light, week here. We could probably get started here in a second, Yeah, if you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you wanted to talk about, go ahead and add them there as well.
And I can jump in here and start sharing my screen.
Cool. Alright.
Yeah, so I think, most people know this, but just KubeCon North America's next week. We are still planning to have a meeting. The Europe folks are gonna hold it down. I don't know, Robert, I'm guessing maybe you take on the lead for the presentation?
**Robert Pająk (Splunk Inc.)** 04:22 Next week, sure. Okay. The alternative is that we can skip, because I think David will be also there, right, at QuickCon.
**Tyler Yahn (Splunk)** 04:32 He will. Yeah, we talked about this… yeah, yeah, we talked about this last week, and Damien said that he wanted to keep it, but, honestly, that's between you and Damien.
If you both decide, like, let's just skip, I mean, that's fine. Just make sure it's posted to the community so no other members show up, thinking that we'll be here, okay?
**Robert Pająk (Splunk Inc.)** 04:51 Okay.
**Tyler Yahn (Splunk)** 04:52 Yeah.
**Robert Pająk (Splunk Inc.)** 04:53 So I'll try to… I'll try to facilitate them next week. Okay. If they mean one at all.
**Tyler Yahn (Splunk)** 04:58 That sounds good.
Perfect.
That being said, I think that, yeah, like, if you are… watching the recording and you're gonna be at KubeCon, please come find us, I think we have, like, one of those… CNCF small booths that we'll be at. I'm guessing there's gonna be some other people there, so… just come to the shop floor, I'm sure, or the vendor floor, and we'll all be somewhere around there.
Yeah.
On that note, though, also on Tuesday next week, if you are gonna be at, KubeCon, please join the ContribFest. It's at… I want to say… 10.30 in the morning, but I'm not 100% sure. I should probably know that better than I do.
But yeah, that's definitely something that, like, as a maintainer, David, please, if you have time and you can make it, please come join. That'd be really helpful, actually.
I can… this is…
**David Ashpole (Google LLC)** 05:59 Trip Fest.
**Tyler Yahn (Splunk)** 06:00 Yeah, ContribFest, it's in the main conference on Tuesday, in the morning.
**David Ashpole (Google LLC)** 06:04 I'm gonna miss the first part, because it conflicts with my talk, but I'll be there towards the second half.
**Tyler Yahn (Splunk)** 06:08 Okay, cool. Yeah, I forgot about that. Yeah, we already talked. That sounds good.
If you also have items or issues that you know could use some help from a brand new member, please go ahead and tag them with ContribFest, and if you needed maybe, say, a reproduction.
That's another item we're asking people to work on at Contra Fest.
Just tag them with an issue label of needs verification.
But yeah, in… make sure that it's unassigned. Additionally, please leave a comment to the effect of telling people not to work on it until after ContribFest, or, yeah, we are trying to hold off on these. There's not really a great process, other than just asking. If you do see a PR open prior to the ContribFest, just close it.
Saying that we're trying to save these, would be ideal.
I think there's something like, 160 in our two repos that I created yesterday, so I don't think there's gonna be a… lack. There's also, like, another 80 from EVPF, so… I think in total we have over 400 issues. I'm not too worried about this, but, Yeah.
it should be, should be good. If you do have more, issues, though, please add them. The best thing we can do is, once this is done, is also just, you know.
remove those comments, and then saying, these are also now really good first-issue comments and getting new contributors, a guideline and a path. A lot of them are really simple issues, like fixing spelling mistakes in docs, so yeah.
If you have other ones, please, please add them.
Okay, moving on. I did have 3 PRs associated with the Finnish, Aware, experimental API and, SDK. These all have reviews from David, which I appreciate. Robert said that he was gonna take a look at these later in the day, so maybe not too much more to mention, other than they just needed reviews. Robert's gonna take a look, so that should be enough. I know Damien's also taking a look at this. Looks like Robert has as well.
I don't know what's going on here.
I will… take a look at this after the meeting, I don't…
**Robert Pająk (Splunk Inc.)** 08:15 Compilation error after merchant.
**Tyler Yahn (Splunk)** 08:18 Oh, really?
**Robert Pająk (Splunk Inc.)** 08:19 Yep.
**Tyler Yahn (Splunk)** 08:21 Yes, looks like this merged already. Okay, so I'm gonna have to fix this up really quick, but, yeah, otherwise it should be good. I'm guessing these probably need to get rebased as well, based on what I just saw. Yeah, okay. So, I'll update these. But yeah, if you haven't yet and you're interested, please take a look. These are pretty close to getting merged, so yeah, they will likely get merged.
Last thing up on that one is just getting the histogram I guess there's ex… Exponential histogram as well.
Which actually shouldn't be too hard. So yeah, a histogram and an exponential histogram, supporting the Finnish API, and then that should be done and ready to get evaluated.
mostly just hooked into OB. And then, I guess also, like, you know, this is going to get pushed back into the spec, OTEP as well, so… I'm guessing I'll probably have to take that over. I don't think Antoine's been working too much on that one, but yeah.
Well, cool, that's what I had for the written agenda. I can pause here. I don't know if other folks had other items they wanted to talk about.
**Robert Pająk (Splunk Inc.)** 09:29 So, one thing that I'll probably, next week, I'll propose some threat model document, and try to enable… create a PER for the OSS.
scanner, the entropic one, but yeah, it will be just… It was… Once there, it will be there, and that was before I just…
**Tyler Yahn (Splunk)** 09:50 Yeah, that sounds great. Yeah, that sounds like it'd be really helpful to some of the work we're already doing for security stuff, Sam.
I saw Puneet just joined as well. Puneet, we're kind of wrapping it up. I don't know if you had anything you wanted to add. I saw your, option conflicting, PR got merged, hence why I gotta rebase this thing. But, also, I don't know if there's anything else, the configurator work, that you wanted to mention. I know you're also out, so… Yeah.
**Puneet Singh** 10:20 Yeah.
So, regarding the option conflicting thing.
Is it… is it about rejecting the… Meter provider build options, once we have, like, multiple experimental types.
**Tyler Yahn (Splunk)** 10:36 Yeah, I think that's what it is. I honestly don't know. We were just talking about the PRs I have for the finished stuff, and I merged in, main, and now the build's failing, so I'm guessing that's where that's coming from. It's on my end, like, I just need to fix it, like, it's… Don't worry about that, that's not really on you. It's more just a side.
**Puneet Singh** 10:53 Alright, just a small thing, actually. So, this PR about rejecting multiple experimental options I was working on. I think a small piece of code has gone in, which kind of… Tests the configurator and the… Ex… view options.
Together.
Sure.
So, David, I have disabled… hello? Sorry. I, I felt like the screen froze.
convertible?
**Tyler Yahn (Splunk)** 11:28 Yeah, you were kind of breaking up there.
Yeah, you broke up. I don't know, you know, maybe if you could just repeat that?
**Puneet Singh** 11:36 Yeah, so I have disabled a test which tries to use the experimental view option with the configurator, because those are, like, two experimental options, which kind of fail, and resulting in the failure, actually, so because of which this PR can't go through, which tries to… Reject multiple experimental options.
Scope.
Have a look.
**Tyler Yahn (Splunk)** 12:03 Yeah, absolutely. That sounds good.
**Puneet Singh** 12:05 So I assume, next week, we won't have any call.
**Tyler Yahn (Splunk)** 12:12 We were talking about that at the beginning, it sounds like Damien had asked for one next week, and then Robert said he was gonna show up and facilitate, so yeah, if you wanted to show up, Robert and Damien I don't know if Damien is officially gonna be here, but, like, the… yeah, there should be a call next week. Robert would enjoy your company.
**Puneet Singh** 12:29 Cool Alright.
**Tyler Yahn (Splunk)** 12:32 Yeah.
He'll probably ask about models, and yeah, he'll be the security expert by the end of the call.
**Puneet Singh** 12:41 That would be cool, yeah.
**Tyler Yahn (Splunk)** 12:43 Yeah, okay.
Awesome, cool.
Well, if there's nothing else from folks, we can end the meeting here.
Looking forward to seeing some of you all next week, and yeah, looking forward to just continuing on.
Definitely will talk, I think, after KubeCon a little bit more about, like, the upcoming year, finishing out the year with our goals, talking about planning as well for next year. So, yeah, start… start thinking about that, I guess is all I'm saying.
**David Ashpole (Google LLC)** 13:14 Yep, good stuff.
Yeah.
**Tyler Yahn (Splunk)** 13:16 Bye, everyone.
**Robert Pająk (Splunk Inc.)** 13:17 Bye.
**Puneet Singh** 13:17 Right.
