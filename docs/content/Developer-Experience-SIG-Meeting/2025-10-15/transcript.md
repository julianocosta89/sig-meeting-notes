SIG: Developer Experience SIG Meeting
Date: 2025-10-15
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/mhJcqsEe8gjurGh-4JXadAAw2Yrjz3lslXaiXbmyKbWMawMIC6IWmn6MhpnRO5mT.WmxhEEqpqSXoF4XT
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 00:41 Hey!
**Juliano Costa | Datadog** 00:43 Hello, hello!
Good morning.
**Damien Mathieu** 00:52 How are you?
**Juliano Costa | Datadog** 00:54 I'm good, how are you?
**Damien Mathieu** 00:57 All good. Yeah, tired, but that's, the life, with, with a baby.
**Juliano Costa | Datadog** 01:05 Well, I think I can relate, so…
Nice.
I finally, have an initial draft of the… Of the blog.
I'm still going through, like, grammar and stuff, but I think,
the main area… I need to wrap up and add, like, one or two minor stuff, but,
But the… the skeleton is there, it's good to say.
**Damien Mathieu** 01:48 Nice.
Nice.
**Juliano Costa | Datadog** 01:53 I… probably later today, we'll post on the channel, so you and Tristan can take a look.
And, so, as Tristan just joined.
**Tristan Sloughter** 02:09 We're talking about?
**Juliano Costa | Datadog** 02:09 look again.
**Tristan Sloughter** 02:10 Oh, cool.
**Juliano Costa | Datadog** 02:12 Yeah, yeah. So I have an initial draft. I think I need to just wrap up stuff, and then kind of conclude and set a hook for the next series of the next post of the series.
But I think I have a nice introduction, so to say. I talk about what Mastodon is, and then their setup, so…
**Tristan Sloughter** 02:38 Wearing a black shirt, so I just realized I'm floating.
**Juliano Costa | Datadog** 02:41 Yeah, that's, awesome.
**Tristan Sloughter** 02:45 Alright, cool.
We might…
all messed up and didn't get back to the person early enough, I think, about having an interview today.
So it might be next Wednesday.
But we can wait a few minutes to see if they join. Let me pull this up.
**Juliano Costa | Datadog** 03:07 I feel that I'm talking with, the… what's the name of the…
Do you know the first Star Ranger? Where they, they talked with the, the thing? Like, is it Gordon? Yeah.
Yeah.
**Tristan Sloughter** 03:22 Yes.
**Juliano Costa | Datadog** 03:24 Awesome. That's you.
Hold up.
But, other than that, any…
One thing that I want to, to call out here,
if you guys open the link that I shared and scroll a bit down, there is a screenshot for…
Pro Taobin.
And… I… I don't know. Should we use that? Should I… should we use Mermaid?
It… it feels too small, to be honest.
**Tristan Sloughter** 04:04 Yeah.
**Juliano Costa | Datadog** 04:04 I don't know…
**Tristan Sloughter** 04:05 Blend.
**Juliano Costa | Datadog** 04:06 If the blog allows people to click and expand, or something like that.
**Tristan Sloughter** 04:11 Oh, really.
**Juliano Costa | Datadog** 04:14 The image itself, let me open here on my… Computer.
It's not big.
So, like, I can read stuff, but still, it's not, like.
I don't know how that would look like in Mermaid.
And, so this is one thing.
The second question is… Do we… do we want to keep their… a vendor.
Or should we just tell vendor, like, because we have the pipelines, and then, like, we have a full example, and then they send the stuff to Datadog?
**Damien Mathieu** 04:57 I…
**Tristan Sloughter** 04:57 Hmm.
**Damien Mathieu** 04:59 wouldn't mention the number of posts. I would just say it's a series of posts.
**Juliano Costa | Datadog** 05:04 Okay, okay.
**Damien Mathieu** 05:05 just, I mean, we may do more interviews in the future, so it can be, like, this is the developer experience,
posts.
**Tristan Sloughter** 05:18 Yep.
**Juliano Costa | Datadog** 05:19 Here is a post, okay. Yeah, that's solved.
**Damien Mathieu** 05:25 And… Oh, God.
I know that the blog does not allow updating, posts retroactively, but I think it would be nice for future ones to link to the previous ones at the start.
**Juliano Costa | Datadog** 05:40 Yeah, that would… Work.
**Tristan Sloughter** 05:45 True.
the… I'm… My initial… Gut reaction was to not… Have vendors in there.
But it's also… but then I was like.
But it is what they're using, so…
It's kind of hard to…
decide… I don't know if maybe we should ask, people who run the blog or something.
Probably not have it.
In any way, we'll be like.
**Damien Mathieu** 06:17 I mean, I'm seeing vendors mentioned.
from time to time in the blog. I think as long as the post is vendor agnostic, and it's not saying, like, you need to use Datadog to do what we're doing, it's fine.
**Tristan Sloughter** 06:34 Alright.
Should be fun.
Hmm.
**Juliano Costa | Datadog** 06:41 Yeah, I think…
from the vendor perspective, it's tricky because they mentioned that one of their pain points is, managing the naming stuff, because of their vendor. So, yeah, they're kind of… not complaining, but yeah, this is one of their pain points.
Well, it's definitely not… only there.
There's, like, there are more customers that face the same, so, it's fine.
But yeah, I feel that if we want to show… Production?
Set up.
We think… I think we need to show what they are using.
**Tristan Sloughter** 07:26 Right.
**Juliano Costa | Datadog** 07:28 I don't know if we have for the other, interviews that we got, like, the full thingy.
the full collector.
**Tristan Sloughter** 07:38 Yeah.
**Juliano Costa | Datadog** 07:38 Wow.
**Tristan Sloughter** 07:39 I know we don't for Atlassian.
**Juliano Costa | Datadog** 07:44 But I think Atlassian is pretty approachable, so we can just ping, the guy. True. Yeah.
He's well involved in the community, so…
**Tristan Sloughter** 07:55 Yep.
**Juliano Costa | Datadog** 07:55 It's not, that hard to, to get them?
Mmm… Okay.
another… another question?
Should I mention, who we interviewed?
**Tristan Sloughter** 08:18 Who the company is? Or the person?
**Juliano Costa | Datadog** 08:20 Yeah, the person?
Like, I have a, mention… I…
**Damien Mathieu** 08:25 would… yes, I would… I would even link to the GDoC profile.
**Juliano Costa | Datadog** 08:31 Cool, okay. Yeah, I added their Mastodon profile, but I can, because, like.
**Tristan Sloughter** 08:39 thing is from Astadon, so… Yeah.
**Damien Mathieu** 08:41 Yeah, but.
**Juliano Costa | Datadog** 08:42 thought about leaking their LinkedIn, but then I said, I don't know, most of them.
**Damien Mathieu** 08:46 I would… I think I would still link GitHub, because, it's… it's Mastodon, it's a social network, but, for other companies, we are going to not be able to do that, so maybe we should do the same every time, so we do GitHub every time.
They can have their Mastodon profile on their GitHub profile. And I think linking to the person who… like, it's… we are saying it's an interview. You cannot have an interview with a company, and that shows that it's actually an interview, and not, like, a marketing stint.
**Tristan Sloughter** 09:23 They didn't thought that they didn't send us a… Blurb for marketing team.
**Juliano Costa | Datadog** 09:32 Cool. Okay.
I don't think I have any… So, like, from my end.
I just need to wrap up the block, and I will try it out to see how the collector config looks like in Mermaid.
That will be a bit more… work for us.
But I think the visualization… I think in Mermaid, we have more ways of visualizing it.
**Tristan Sloughter** 10:05 Room.
**Juliano Costa | Datadog** 10:05 Bob.
And…
**Tristan Sloughter** 10:07 Yeah.
That might be nice.
**Juliano Costa | Datadog** 10:09 we may lose, like, their icons and stuff, which is cool from Autobi, but I… I don't know.
I'm… I'm open to, to opinions, like…
I could even try to reach out to them and see if we can export this in any way, like…
**Tristan Sloughter** 10:30 Yeah, I was gonna say, do they have… they don't have any… they just have images?
That you could see for export.
Or is this even a screen grab, or is this an export?
**Juliano Costa | Datadog** 10:41 It's like, I have a share button, and then I can download image.
I think if I do this, the links will be… It has more than… It has.
5,000 characters.
Zoom doesn't allow me to.
toothpaste. But let me… let me share this screen.
So this is what I have here.
And… if I… share, I can download the image, that's it.
Hmm, but then, like… Let me turn you.
Like, I can… X-Pen, but, like… That's it.
**Tristan Sloughter** 11:44 Let me see,
I wonder if… so I'm checking if… because…
Last I know, we were using Hugo.
And maybe that has a quick short code for… Expand image.
I might be able to, even if it's not already in…
Our blog, we might be able to include it, and they'd be fine with it.
**Juliano Costa | Datadog** 12:23 Yeah, and we have an open issue on the demo where people are complaining about the screenshots from Jaeger and Grafana, and I think they are currently working on the click to expand, because that feature is not there at the moment.
**Tristan Sloughter** 12:40 I mean, you can also just make it a link, but… Open a new…
**Juliano Costa | Datadog** 12:45 you have with it.
**Tristan Sloughter** 12:55 Not finding anything quickly.
Oh, I found a blog post that says they have it.
**Juliano Costa | Datadog** 13:07 And here'll go…
**Tristan Sloughter** 13:09 Yeah.
**Juliano Costa | Datadog** 13:10 Okay.
**Tristan Sloughter** 13:15 Whoa.
It'd be nice if they created it.
short code out of this, but I can…
Just a little bit of JavaScript.
Oh, some Cloudflare JavaScript… I mean, not… CDN, but the…
some JavaScript library, so who knows if that's okay to just pull in? I don't know.
**Juliano Costa | Datadog** 13:45 I see.
**Tristan Sloughter** 13:52 I think that would be… If we can, you know, get this…
the blog people are okay with it. I think, yeah, the click-to-Zoom would be the easiest, and… Nicest solution?
**Juliano Costa | Datadog** 14:04 Okay.
Yeah, then, yeah, definitely easier, because, thinking that we… we will have to do that… the same process for…
**Tristan Sloughter** 14:15 Yeah.
**Juliano Costa | Datadog** 14:15 3 or 4 more?
**Tristan Sloughter** 14:18 Right.
**Juliano Costa | Datadog** 14:21 blocks, then it's, yeah, okay.
**Tristan Sloughter** 14:28 And yeah, so, like, Atlassian, if they…
like, Mastodon, they just, like, gave you the collector configuration, right? Or a… Yep. Yeah.
I think when Mastodon, They're probably…
They wouldn't do that, but maybe they'd just give us, like, a list of… the…
components they use, and then I can just make a collector configuration out of it and put it in the hotel bin, so…
Well, we don't need… because, like, OTELDIN shows anything, like, the configuration parts, options, so I can just plug that in, probably, and… so we won't have the actual thing, but we can have it.
Display it the same way that you.
I assume they do that.
Hopefully.
**Juliano Costa | Datadog** 15:13 What we could maybe ask is for the pipelines.
**Tristan Sloughter** 15:18 Because in the pipeline, they… they…
**Juliano Costa | Datadog** 15:21 They have all the components, and they do not have any configuration on that, so…
**Tristan Sloughter** 15:26 Yep, doesn't show anything else. Yeah.
**Juliano Costa | Datadog** 15:28 No.
**Tristan Sloughter** 15:29 Assuming they're… yeah.
I could also see a company not wanting to put the vendor in there, but… We can just…
replace that with vendor. Tell them they can just… if they don't, they can just put… Vendor.
**Juliano Costa | Datadog** 15:42 Yeah, we can do it vendor or OTLP.
**Tristan Sloughter** 15:46 Yeah, yeah.
Yeah, don't have to say where it's going.
**Juliano Costa | Datadog** 15:50 Yup.
**Tristan Sloughter** 15:54 Man, I can't remember who they used. It's not in the notes I have.
Boom.
So you mentioned, when I joined, you were saying you…
put a link in the chat. Were you saying, do… should we, review… What you have right now.
**Juliano Costa | Datadog** 16:16 No, no, I, I…
**Tristan Sloughter** 16:18 Are you gonna…
**Juliano Costa | Datadog** 16:18 So if you can, just have this tab open, because I will not share this link on,
on the channel later, but okay. Later today, probably before I wrap up for lunch, I'll…
I'll ping you guys for our initial review, so…
**Tristan Sloughter** 16:38 Alright, sounds good.
**Juliano Costa | Datadog** 16:40 Nope.
**Tristan Sloughter** 16:43 Good.
**Juliano Costa | Datadog** 16:44 Yes, and sorry for taking long, yeah, I had a couple of, conferences in the… in the middle.
**Tristan Sloughter** 16:50 Yeah, you've been… Getting the word out, so…
You guys have anything else, or…
Should we call here and review later today?
**Damien Mathieu** 17:03 I don't have anything else.
**Tristan Sloughter** 17:06 Alright.
Awesome.
**Juliano Costa | Datadog** 17:10 Vince, you guys.
**Tristan Sloughter** 17:13 Yep.
Bottom line.
**Juliano Costa | Datadog** 17:15 Later.
**Tristan Sloughter** 17:16 Excellent.
**Juliano Costa | Datadog** 17:17 But…
